"""
一般 Python 用于连接 MySQL 的工具：pymysql
"""
import pymysql.cursors
import configparser

# cf = configparser.ConfigParser()
# cf.read("D:\ProgramFiles\JetBrains\PyCharm 2019.1.1\projects\music-163\config.ini")

connection = pymysql.connect(host='rm-wz9n465jay97249bzwo.mysql.rds.aliyuncs.com',
                                  user='hyh',
                                  password='19980218Hyh',
                                  db='hdb',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

# 获取表的字段名
def get_params(connection0,table):
    with connection0.cursor() as cursor:
        sql = "select * from %s "
        cursor.execute(sql%table)
        list = []
        for i in cursor.description:
            list.append(i[0])
    connection0.commit()
    print(list)
table = "comments"
print(table)
get_params(connection,table)

#保存推荐歌单
def insert_playlist(id,type,name,copywriter,picUrl,canDislike,trackNumberUpdateTime,playCount,trackCount,highQuality,alg):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `comments` (`id`,`type`,`name`,`copywriter`,`picUrl`,`canDislike`,`trackNumberUpdateTime`,`playCount`,`trackCount`,`highQuality`,`alg`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(id,type,name,copywriter,picUrl,canDislike,trackNumberUpdateTime,playCount,trackCount,highQuality,alg))
    connection.commit()


# 保存评论
def insert_comments():
    with connection0.cursor() as cursor:
        sql = "INSERT INTO `recommend_playlist` (`MUSIC_ID`, `COMMENTS`, `DETAILS`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, comments, detail))
    connection0.commit()


# 保存音乐
def insert_music(music_id, music_name, album_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `musics` (`MUSIC_ID`, `MUSIC_NAME`, `ALBUM_ID`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, music_name, album_id))
    connection.commit()


# 保存专辑
def insert_album(album_id, artist_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `albums` (`ALBUM_ID`, `ARTIST_ID`) VALUES (%s, %s)"
        cursor.execute(sql, (album_id, artist_id))
    connection.commit()


# 保存歌手
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


# 获取所有歌手的 ID
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT `ARTIST_ID` FROM `artists` ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有专辑的 ID
def get_all_album():
    with connection.cursor() as cursor:
        sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有音乐的 ID
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取前一半音乐的 ID
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取后一半音乐的 ID
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()
