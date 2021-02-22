import urllib.request
import re
import csv
import datetime
import argparse

def image_hits(self):

    css_counter = 0
    png_counter = 0
    gif_counter = 0
    jpg_counter = 0
    jpeg_counter = 0
    png_counter = 0
    html_counter = 0

    #created counters for each cateogry and used regular expression to find each category from records.
    for i in self:
        if re.search(r"\.css$|\.CSS$", i):
            css_counter +=1
        elif re.search(r"\.png$|\.PNG$", i):
            png_counter +=1
        elif re.search(r"\.gif$|\.GIF$", i):
            gif_counter +=1
        elif re.search(r"\.jpg$|\.JPG$", i):
            jpg_counter +=1
        elif re.search(r"\.jpeg$|\.JPEG$", i):
            jpeg_counter +=1
        elif re.search(r"\.html$|\.HTML$", i):
            html_counter +=1

    total_request = css_counter+png_counter+gif_counter+jpg_counter+jpeg_counter+html_counter
    image_request = (png_counter+gif_counter+jpg_counter+jpeg_counter)/total_request*100
    total_hits = png_counter+gif_counter+jpg_counter+jpeg_counter+png_counter
    print("="*100)
    print("Image requests account for " + str(round(image_request)) + "% and " + str(total_hits) + " hits of all requests.")
    print("png request account for " + str(round(png_counter / total_request * 100)) + "% and " + str(png_counter) + " hits of all requests.")
    print("gif request account for " + str(round(gif_counter / total_request * 100)) + "% and " + str(gif_counter) + " hits of all requests.")
    print("jpg request account for " + str(round(jpg_counter/ total_request * 100)) + "% and " + str(jpg_counter) + " hits of all requests.")
    print("jpeg request account for " + str(round(jpeg_counter/ total_request * 100)) + "% and " + str(jpeg_counter) + " hits of all requests.")
    print("png request account for " + str(round(png_counter / total_request * 100)) + "% and " + str(png_counter) + " hits of all requests.")

def popular_browser(self):
    print("=" * 100)
    Chrome = 0
    IE = 0
    Firefox = 0
    Safari = 0

    for i in self:
        #The kernel of the Chrome browser is developed by AppleWebKit, so the name of the browser and the kernel will be written on the weblog.
        if re.search(r"Chrome/.*? Safari", i):
            Chrome +=1
        elif re.search(r"MSIE", i):
            IE +=1
        elif re.search(r"Firefox", i):
            Firefox +=1
        #Only data with Safari keyword alone in records are belong to the Safari users
        elif re.search(r"Safari/", i):
            Safari +=1


    print("Chrome users: " + str(Chrome), ";IE users: " + str(IE), ";Firefox users: " + str(Firefox), ";Safari users:" + str(Safari))

    #find out the max number
    if Chrome > IE and Chrome > Firefox and Chrome > Safari:
        print("Chrome is the most popular browser.")
    elif IE > Chrome and IE > Firefox and IE > Safari:
        print("IE is the most popular browser.")
    elif Firefox > Chrome and Firefox > IE and Firefox > Safari:
        print("Firefox is the most popular browser.")
    elif Safari > Chrome and Safari > IE and Safari > Firefox:
        print("Safari is the most popular browser.\n")


def hit_per_hour(self):
    print("=" * 100)
    time_list=[]

    #Splited dateime records with " " delimiter and extracted %H%M%S data only
    for i in self:
        time_list.append(i.split(" "))

    n = 1
    time_list=[i[n] for i in time_list]

    hour_00,hour_01,hour_02,hour_03,hour_04,hour_05,hour_06,hour_07,hour_08,hour_09,hour_10,hour_11,hour_12,hour_13,hour_14,hour_15,hour_16,hour_17,hour_18,hour_19,hour_20,hour_21,hour_22,hour_23,hour_24,= 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    for i in time_list:
        #Converted the datetime to show hour only
        if datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "01":
            hour_01 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "02":
            hour_02 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "03":
            hour_03 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "04":
            hour_04 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "05":
            hour_05 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "06":
            hour_06 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "07":
            hour_07 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "08":
            hour_08 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "09":
            hour_09 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "10":
            hour_10 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "11":
            hour_11 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "12":
            hour_12 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "13":
            hour_13 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "14":
            hour_14 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "15":
            hour_15 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "16":
            hour_16 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "17":
            hour_17 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "18":
            hour_18 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "19":
            hour_19 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "20":
            hour_20 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "21":
            hour_21 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "22":
            hour_22 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "23":
            hour_23 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "24":
            hour_24 +=1
        elif datetime.datetime.strptime(i, "%H:%M:%S").strftime("%H") == "00":
            hour_00 +=1

    print("Hour 00 has " + str(hour_00) + " hits.")
    print("Hour 01 has " + str(hour_01) + " hits.")
    print("Hour 02 has " + str(hour_02) + " hits.")
    print("Hour 03 has " + str(hour_03) + " hits.")
    print("Hour 04 has " + str(hour_04) + " hits.")
    print("Hour 05 has " + str(hour_05) + " hits.")
    print("Hour 06 has " + str(hour_06) + " hits.")
    print("Hour 07 has " + str(hour_07) + " hits.")
    print("Hour 08 has " + str(hour_08) + " hits.")
    print("Hour 09 has " + str(hour_09) + " hits.")
    print("Hour 10 has " + str(hour_10) + " hits.")
    print("Hour 11 has " + str(hour_11) + " hits.")
    print("Hour 12 has " + str(hour_12) + " hits.")

    print("Hour 13 has " + str(hour_13) + " hits.")
    print("Hour 14 has " + str(hour_14) + " hits.")
    print("Hour 15 has " + str(hour_15) + " hits.")
    print("Hour 16 has " + str(hour_16) + " hits.")
    print("Hour 17 has " + str(hour_17) + " hits.")
    print("Hour 18 has " + str(hour_18) + " hits.")
    print("Hour 19 has " + str(hour_19) + " hits.")
    print("Hour 20 has " + str(hour_20) + " hits.")
    print("Hour 21 has " + str(hour_21) + " hits.")
    print("Hour 22 has " + str(hour_22) + " hits.")
    print("Hour 23 has " + str(hour_23) + " hits.")
    print("Hour 24 has " + str(hour_24) + " hits.")

def downloadData(self):
    lines=[]
    path_to_file=[]
    browser=[]
    time=[]

    #Initiated a web request through ulropen method from urllib package
    with urllib.request.urlopen(self) as response:

        #read and decode the html with 'utf-8'
        weblog = response.read().decode('utf-8')
        weblog_lines = weblog.split("\r\n")

        #removed the footer
        weblog_lines.pop(len(weblog_lines)-1)

        #Used the csv module to read the information of each column in csv file
        csv_reader = csv.reader(weblog_lines, delimiter=',')

        #Extracted path, browser, and time information from columns and put them in different lists for futher processing
        for lines in csv_reader:
            path_to_file.append(lines[0])
            browser.append(lines[2])
            time.append(lines[1])

        image_hits(path_to_file)
        popular_browser(browser)
        hit_per_hour(time)



if __name__ == '__main__':

    #url= 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

    #Accepted a parameter from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    downloadData(args.url)





