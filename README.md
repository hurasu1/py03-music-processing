# pythonにおける音楽処理ライブラリ

## 目的
データ（例えば、sin波）から音をスピーカーなどで鳴らせるようなライブラリを調査して、
使えるようになる。



## 音楽ライブラリ
python公式webページに色々あると記載がある。
- https://wiki.python.org/moin/Audio/

他の人がつかっていそうなもの
- music21
    + midiやmusicXMLは扱えるが、mp3やwaveは無理そう。
    + https://qiita.com/ognek/items/924ca96f0c4be4ed0e24
    + https://stackoverflow.com/questions/46394954/is-it-possible-to-analyze-mp3-file-using-music21
- Librosa
    + mp3など扱える

## librosaを使ってみる
### install & 環境構築
pythonのlibraryをinstallする。
```shell script
pip install librosa
pip install matplotlib
```
