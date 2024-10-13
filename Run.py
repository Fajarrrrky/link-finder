import os, re, requests, json, time

COOKIES = {
	'Cookie': 'Tempel cookie disini'
}

GET, Loop = [], 0

M = '\x1b[1;91m'
P = '\033[0m'
H = "\033[32m"

class asset:
    
    def headers_get(self):
        return {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
             'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             'dpr': "2.75",
             'viewport-width': "980",
             'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
             'sec-ch-ua-mobile': "?0",
             'sec-ch-ua-platform': "\"Linux\"",
             'sec-ch-ua-platform-version': "\"\"",
             'sec-ch-ua-model': "\"\"",
             'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
             'sec-ch-prefers-color-scheme': "light",
             'upgrade-insecure-requests': "1",
             'sec-fetch-site': "same-origin",
             'sec-fetch-mode': "navigate",
             'sec-fetch-user': "?1",
             'sec-fetch-dest': "document",
             'referer': "https://www.threads.net/",
             'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }
    
    def requ_headers(self):
        return {
          'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
          'Content-Type': "application/x-www-form-urlencoded",
          'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
          'sec-ch-ua-model': "\"\"",
          'x-ig-app-id': "238260118697367",
          'sec-ch-ua-mobile': "?0",
          'x-fb-friendly-name': "BarcelonaSearchResultsRefetchableQuery",
          'x-fb-lsd': "59xbOnglEiiNF-bxNeTf3D",
          'sec-ch-ua-platform-version': "\"\"",
          'x-asbd-id': "129477",
          'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
          'sec-ch-prefers-color-scheme': "light",
          'x-csrftoken': "sWac0NFOlgZkQxyeSAIoAmrT4IiDuOCO",
          'sec-ch-ua-platform': "\"Linux\"",
          'origin': "https://www.threads.net",
          'sec-fetch-site': "same-origin",
          'sec-fetch-mode': "cors",
          'sec-fetch-dest': "empty",
          'referer': "https://www.threads.net/search?q=lagi%20sebar%20dana&serp_type=default",
          'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }
    def get_data(self, req):
        return {
          "av": re.findall('"actorID":"(\d+)"', req)[0],
          "__user": "0",
          "__a": "1",
          "__req": "2l",
          "__hs": re.findall('"haste_session":"(.*?)"', req)[0],
          "dpr": "3",
          "__ccg": "UNKNOWN",
          "__rev": re.findall('"__spin_r":(\d+)', req)[0],
          "__s": "",
          "__hsi": re.findall('"hsi":"(\d+)"', req)[0],
          "__dyn": "",
          "__csr": "",
          "__comet_req": "29",
          "fb_dtsg": re.findall('\["DTSGInitialData",\[\],\{"token":"(.*?)"\},\d+\]', req)[0],
          "jazoest": re.findall('jazoest=(\d+)', req)[0],
          "lsd": re.findall('\["LSD",\[\],{"token":"(.*?)"},\d+]', req)[0],
          "__spin_r": re.findall('"__spin_r":(\d+)', req)[0],
          "__spin_b": "trunk",
          "__spin_t": re.findall('"__spin_t":(\d+)', req)[0],
          "__jssesw": "2",
        }

class main:

    def cari_link(self):
        try:
            with requests.Session() as r:
                cookie = COOKIES['Cookie']
                key = input(f" {H}#{P} keyword: ")
                try:
                    delay = int(input(f" {H}#{P} Masukkan waktu delay antar request (detik, default 20): ") or 20)
                except ValueError:
                    print(f"{M}Input tidak valid, menggunakan delay default: 20 detik{P}")
                    delay = 20
                max_links = int(input(f" {H}#{P} Batas jumlah tautan yang ditemukan (default 50): ") or 50)
                for value in key.split(','):
                    query = {"q": value, "serp_type": "default"}
                    response = r.get('https://www.threads.net/search', params=query, headers=asset().headers_get(),cookies={'cookie': cookie}).text
                    data = asset().get_data(response)
                    self.next_cari_link(value, delay, data, cookie, '', max_links)
        except Exception as e:
            pass

    def next_cari_link(self, query, delay, data, coki, after, max_links):
        global Loop
        try:
            with requests.Session() as r:
                headers = asset().requ_headers()
                data.update({
                    "fb_api_caller_class": "RelayModern",
                    "fb_api_req_friendly_name": "BarcelonaSearchResultsRefetchableQuery",
                    "variables": json.dumps({"after":after,"before":None,"first":10,"last":None,"meta_place_id":None,"pinned_ids":None,"query":query,"recent":0,"search_surface":"default","tagID":None,"__relay_internal__pv__BarcelonaIsLoggedInrelayprovider":True,"__relay_internal__pv__BarcelonaIsInlineReelsEnabledrelayprovider":True,"__relay_internal__pv__BarcelonaOptionalCookiesEnabledrelayprovider":True,"__relay_internal__pv__BarcelonaShowReshareCountrelayprovider":True,"__relay_internal__pv__BarcelonaQuotedPostUFIEnabledrelayprovider":False,"__relay_internal__pv__BarcelonaIsCrawlerrelayprovider":False,"__relay_internal__pv__BarcelonaShouldShowFediverseM075Featuresrelayprovider":False}),
                    "server_timestamps": "true",
                    "doc_id": "8829346373783415"
                })
                headers.update({
                    'x-fb-lsd': data.get('lsd'),
                    'x-csrftoken': re.search("csrftoken=(.*?);", str(coki)).group(1),
                    'cookie': coki,
                })
                post = r.post('https://www.threads.net/api/graphql', cookies={'cookie': coki}, data=data, headers=headers)
                if post.status_code == 200:
                    if '"searchResults":' in post.text:
                        json_post = json.loads(post.text)
                        link = re.findall(r'https://link\.dana\.id/kaget\?c=([a-zA-Z0-9]+)', str(json_post))
                        print(f' {H}#{P} {len(link)} tautan berhasil ditemukan', end='\r')
                        time.sleep(1.5)
                        for code in link:
                            if Loop >= max_links:
                                print(f" {M}# Batas tautan tercapai: {max_links} tautan{P}")
                                return
                            done = open("Data/Done.txt", "r+").read().splitlines()
                            url = f"https://link.dana.id/kaget?c={code}"
                            if str(url) in GET or str(url) in done:
                                continue
                            else:
                                Loop += 1
                                print(f' {H}#{P} {Loop} link: {H}{url}{P}')
                                GET.append(url)
                                print(f' {H}#{P} menemukan: {H}{code}{P}{" "*16}', end='\r')
                                time.sleep(0.5)
                                for sleep in range(int(delay), 0, -1):
                                    print(f" {H}#{P} tunggu: {M}{sleep}{P}{' '*40}", end='\r')
                                    time.sleep(1)
                                with open('Data/Done.txt', 'a+') as g:
                                    g.write(f'{url}\n')
                                g.close()
                        if json_post["data"]["searchResults"]["page_info"]["has_next_page"]:
                            next = ["data"]["searchResults"]["page_info"]["end_cursor"]
                            self.next_cari_link(query, delay, data, coki, next, max_links)
        except Exception as e:
            pass

if __name__ == '__main__':
    os.system('clear')
    main().cari_link()