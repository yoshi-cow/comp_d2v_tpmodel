# comp_d2v_tpmodel
Doc2VecとTopicModelによるクラスタリング結果を比較するために作成したプログラミングです。  
４人の作家の文学作品を用意し、それぞれでクラスタリングを行い作家毎にクラスタリングされているかを比較しました。 
カウントベースと推論ベースで純文学を処理させた場合にどう違いがでるか調べています。  
（Doc2Vecでベクトル化しKmeansでクラスタリングしたものと、TopicModelでトピックわけした結果を比較しています。）

## クラスタリング対象データ  
- 梶井基次郎　４５作品  
- 永井荷風　　８５作品  
- 中島敦　　　２７作品  
- 夏目漱石　　１０４作品  

## 結果  
![kekka](https://user-images.githubusercontent.com/61402011/76580630-f6f11480-6513-11ea-92b1-ade1c3784038.png)  
作品数の少ない梶井基次郎と中島敦の作品は、どちらもうまくわけられていませんでした。  
一方で、作品数が多い永井荷風と夏目漱石の作品は、Doc2Vecではいい具合にわけられていました。  
単語の生起確率を求めるモデルよりも、単語の発生を推論するモデルの方が文学上の言い回しとかうまく処理できるとかあるのでしょうか？まだまだ理解が及びません。  

## 環境  
- 小説スクレイピング： ubuntu 18.04.4 / python 3.7.6  
- D2C,TopicModel：Google Colaboratory  

## ファイル内容  
- get_novel ディレクトリ：小説スクレイピング用にscrapyを利用しました。scrapy関連ファイルが入っています。  
- Doc2Vec.ipynb：Google Colabで作成した、D2Vモデル作成に関するjupyter notebookファイルです。  
- topic_model.ipynb：Google Colabで作成した、topicmodel作成に関するjupyter notebookファイルです。



