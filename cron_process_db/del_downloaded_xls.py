'''
删除 mysql kindle_note 数据库中 export_upload_record 数据表中 download_status == '已下载' 的 xls 文件
'''
import pymysql
import os
import traceback


'''
从数据库 export_upload_recode 表获取 download_status == '已下载' 的记录
'''
def get_record_from_sqlite():
    file_list = []
    conn = pymysql.connect(host = 'localhost', user = 'root', password = 'xqksj', database = 'kindle_note', charset = 'utf8')
    try:
        cursor = conn.cursor()
        # 筛选 未经历过 导出的记录 （除去 已导出 和 导出异常 的)
        cursor.execute('SELECT id, export_name FROM export_upload_record WHERE download_status="已下载" AND is_deleted!="已删除";')
        result = cursor.fetchall()

        for rel in result:
            tmp = {'id': rel[0], 'name': rel[1]}
            file_list.append(tmp)
    except Exception as e:
        traceback.print_exc()
    finally:
        conn.close()
        return file_list


'''
并更新其记录为 ‘已删除’
'''
def update_download_status(r_id):
    conn = pymysql.connect(host = 'localhost', user = 'root', password = 'xqksj', database = 'kindle_note', charset = 'utf8')
    status_code = 0
    try:
        cursor = conn.cursor()
        sql = "UPDATE export_upload_record SET is_deleted='%s' WHERE id=%s;"
        cursor.execute(sql % ('已删除', str(r_id)) )
        conn.commit()
        status_code = 1
    except Exception as e:
        conn.rollback()
        traceback.print_exc()
        status_code = -1
    finally:
        conn.close()

    return status_code



'''
Kindle 生词本 导出附件 发送邮箱后自动删除
'''
def delete_file(full_path_file):
    try:
        cmd = 'rm "' + full_path_file + '"'
        os.system(cmd)
        print(cmd)
        print('-> "' + full_path_file + '" 【已删除】')
    except Exception as e:
        traceback.print_exc()
        print('-> "' + full_path_file + '" 【删除失败】')



def main():
    download_path = '/Users/lynn/Desktop/Personal Projects/Kindle_导出生词本_web/kindle_notes/kindle_note/static/exported_files/'

    downloaded_files = get_record_from_sqlite()

    if not len(downloaded_files):
        print('没有找到 已下载 且 未删除 的导出文件')
    else:
        for d_file in downloaded_files:
            print('===============')
            print(d_file)
            delete_file(download_path + d_file['name'])
            status_code = update_download_status(d_file['id'])
            if status_code == 1:
                print('更新 is_deleted 成功')
            else:
                print('更新 is_deleted 失败 !!')
            print('\n')

    print('down')

main()
