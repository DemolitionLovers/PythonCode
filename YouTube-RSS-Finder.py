import os
import sys
import requests



def usage():
    exit('< argument error >')



def request_write(url):
    ldir = os.listdir('.')
    if 'http://' in url or 'https://' in url:
        r = requests.get(url)
        output_filename = 'output-rss-finder.tmp'
        if output_filename in ldir:             # incase not removed
            os.system(f'chmod 600 {output_filename}')  # permisions
        with open(output_filename, 'w') as f:
            f.write(r.text)                     # truncate the file
        return output_filename
    else:
        usage()



def youtube_id(url):
    if 'https://www.youtube.com/channel/UC' in url:
        output_url = url.replace('/channel/', '/feeds/videos.xml?channel_id=')
        print(output_url)
    else:
        found_id = 0
        with open(output_filename, 'r') as f:
            channel_page = f.read().split('"')
            for index, line in enumerate(channel_page):
                # if 'channel_id' in line:
                # if 'externalId' in line:
                if 'rssUrl' in line:
                    print(f'[+]: ID FOUND! https://www.youtube.com/feeds/videos.xml?channel_id={channel_page[index + 2]}')
                    found_id = 1
                    break
        if found_id == 0:
            print('[-]: id not found...')
        if found_id == 1:
            os.system(f'rm -f {output_filename}') # finally...



def bitchute_id(output_filename):
    found_id = 0
    with open(output_filename, 'r') as f:
        channel_page = f.read().split('"')
        for line in channel_page:
            if '/channel/' in line and not 'bitchute.com' in line:
                line = line.replace('/channel/', '/feeds/rss/channel/')
                line = 'https://www.bitchute.com' + line
                exit(line)
                print(f'[+]: ID FOUND! {line}')
                found_id = 1
                break
    if found_id == 0:
        print('[-]: id not found...')
    if found_id == 1:
        os.system(f'rm -f {output_filename}') # finally...



def main():
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        usage()
    if 'https://www.youtube.com/channel/UC' in url:
        youtube_id(url)
    elif 'bitchute.com' in url:
        output_filename = request_write(url)
        if output_filename != None:
            bitchute_id(output_filename)
        else:
            usage()
    else:
        usage()



if __name__ == '__main__':
    main()
