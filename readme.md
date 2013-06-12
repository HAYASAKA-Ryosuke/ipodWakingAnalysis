ipodの万歩計データ管理（ipod nano第7世代）
==========================================

#はじめに
ipod nano第7世代の万歩計機能をcsv化してまとめるものです．
そのうちipodを接続したら勝手にローカルホスト上のhtmlにでもグラフ表示できたら良いなという具合で作ってます．

#使い方
OSXではipodnanoに接続すると
/Volumes/ipod_nanoの名前/iPod_Control/Device/Trainer/Workouts/Empeds/pedometer/synched/
以下にxmlファイル形式で万歩計データがあります．
ここにあるxmlファイルをpythonスクリプトに読み込ませて時系列順にcsvファイル化します．
現段階ではディレクトリを指定させずにpythonスクリプトと同じディレクトリにあるxmlのみを読み込むように作ってます．


