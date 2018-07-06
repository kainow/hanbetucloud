from flickrapi import FlickrAPI #フリッカーのAPIを読み込む
from urllib.request import urlretrieve #urllibの中のリクエストファイルからurlretrieveをインポート
from pprint import pprint #データを表示するため
import os,time, sys #OSの情報を得る

key="ad95e8b31a308ec9fcc8fc3580166028"
secret = "b7c41ed1fefd15e9"
wait_time = 0.3 #待ち時間を設定する

#保存フォルダを指定
cloudname = sys.argv[1] #コマンドラインで入力した情報の二番目
savedir ="./" + cloudname #現在のフォルダの中にある上記の場所に保存

#フリッカーのAPIにアクセス
flickr = FlickrAPI(key, secret, format='parsed-json')#フリッカーAPIにアクセスする変数
result = flickr.photos.search(#命令を実行していく検索時のパラメーターを与える
    text = cloudname, 
    per_page = 100, #個数
    media = 'photos', #検索するデータの種類
    sort = 'relevance', #データのソート順は関連順
    safe_search = 1,#セーフサーチは有効
    extras = 'url_q, licence',#取得したいオプション値画像のアドレスが入っているデータとライセンス情報

)

photos = result['photos']#キーに入っているデータを取得
#pprint(photos)

#各データを順番にダウンロードしていく
for i, photo in enumerate(photos['photo']):#１つ１つのデータをフォトに格納、番号を生成
    url_q = photo['url_q']#各フォトのデータ内のurl_qを入れる
    filepath = savedir + '/' + photo['id'] + '.jpg'#ファイルを生成するためのパスを作成
    if os.path.exists(filepath):continue#ファイルが存在していれば次に行く
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)#ウェイトタイムの時間だけまつ変数