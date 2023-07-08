# distance_sensor_GP2D12
this program will make analog output of position sensor to distance(cm).

# hardware
xiao rp2040

# MEMO
1. センサを２ｃｍの高さの箱の上に置き、センサの光を反射させるための高さ５ｃｍｘ幅１０～２０ｃｍ程度の長方形の箱をターゲットとして用意する。
2. 定規を使ってターゲットの位置を変えながら、その時のＡＤ値を記録する。（ADpushbutton.pyを使うと簡単）
3. 距離とADの関係をグラフにプロットし、近似式を計算。近似多項式などを使ってもいいが、今回は区間を区切って線形補完することにした。

