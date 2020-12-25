# -*- coding: UTF-8 -*-
import xlwt
import time
import random

style_title = 0
style_1 = 0
style_2 = 0
style_pass = 0
style_fail = 0

def init_palette(book):
    xlwt.add_palette_colour("title_blue", 0x8)
    book.set_colour_RGB(0x8, 89, 134, 175)

    xlwt.add_palette_colour("font_grey", 0x9)
    book.set_colour_RGB(0x9, 64, 64, 64)

    xlwt.add_palette_colour("borders_grey", 0xa)
    book.set_colour_RGB(0xa, 128, 128, 128)

    xlwt.add_palette_colour("content_blue", 0xb)
    book.set_colour_RGB(0xb, 215, 237, 245)

    xlwt.add_palette_colour("pass_green", 0xc)
    book.set_colour_RGB(0xc, 45, 163, 56)

    xlwt.add_palette_colour("fail_red", 0xd)
    book.set_colour_RGB(0xd, 207, 53, 53)

def init_style():
    global style_title
    global style_1
    global style_2
    global style_pass
    global style_fail

    style_title = xlwt.easyxf('pattern: pattern solid, fore_colour title_blue;'
                         'font: color 1, bold True;'
                         'borders: left 1, left_colour borders_grey, right 1, right_colour borders_grey, top 1, top_colour borders_grey, bottom 1, bottom_colour borders_grey;'
                         'alignment: horz center, vertical center, wrap 1')

    style_1 = xlwt.easyxf('pattern: pattern solid, fore_colour 1;'
                              'font: color font_grey, bold False;'
                              'borders: left 1, left_colour borders_grey, right 1, right_colour borders_grey, top 1, top_colour borders_grey, bottom 1, bottom_colour borders_grey;'
                              'alignment: horz center, vertical center, wrap 1')

    style_2 = xlwt.easyxf('pattern: pattern solid, fore_colour content_blue;'
                          'font: color font_grey, bold False;'
                          'borders: left 1, left_colour borders_grey, right 1, right_colour borders_grey, top 1, top_colour borders_grey, bottom 1, bottom_colour borders_grey;'
                          'alignment: horz center, vertical center, wrap 1')

    style_pass = xlwt.easyxf('pattern: pattern solid, fore_colour pass_green;'
                          'font: color 1, bold True;'
                          'borders: left 1, left_colour borders_grey, right 1, right_colour borders_grey, top 1, top_colour borders_grey, bottom 1, bottom_colour borders_grey;'
                          'alignment: horz center, vertical center, wrap 1')

    style_fail = xlwt.easyxf('pattern: pattern solid, fore_colour fail_red;'
                             'font: color 1, bold True;'
                             'borders: left 1, left_colour borders_grey, right 1, right_colour borders_grey, top 1, top_colour borders_grey, bottom 1, bottom_colour borders_grey;'
                             'alignment: horz center, vertical center, wrap 1')

def init_title(sheet):
    timestamp = time.time()
    sheet.write(0, 0, '', style=style_title)
    sheet.row(0).height_mismatch = True
    sheet.row(0).height = 256 * 3
    for i in range(1,21):
        timestamp += 86400
        time_stru = time.localtime(timestamp)
        sheet.col(i).width = 256 * 15
        sheet.write(0, i, '%d年\n%d月%d日' % (time_stru.tm_year,time_stru.tm_mon,time_stru.tm_mday), style=style_title)

def set_content(sheet):
    for row in range(1,41):
        if row % 2 == 0:
            style_content = style_2
        else:
            style_content = style_1
        sheet.row(row).height_mismatch = True
        sheet.row(row).height = 280
        sheet.write(row, 0, row, style=style_content)
        for col in range(1,21):
            value = random.randint(0,100000)
            if value < 1000:
                style_content = style_fail
            elif value >99000:
                style_content = style_pass
            elif row % 2 == 0:
                style_content = style_2
            else:
                style_content = style_1
            sheet.write(row, col, value, style=style_content)


workbook = xlwt.Workbook(encoding = 'utf-8')
sheet_1 = workbook.add_sheet('测试结果 1')

init_palette(workbook)
init_style()
init_title(sheet_1)

set_content(sheet_1)

filepath = 'D:\\'
filename = time.strftime("%Y%m%d%H%M%S", time.localtime())+'.xls'
workbook.save(filepath+filename)