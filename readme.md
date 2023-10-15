# Volumetric Glassware for Python
Do you have some annoyances to calculate uncertainty?
if so this project may help you.
This project is going to be representation of glasswares in Python.

不確かさの取り扱いで頭を悩ませたことは？
そうならこのプロジェクトは多分役に立つでしょう。
このプロジェクトはガラス器具をPython言語で写像したものです。

# Single Marked Glassware
Volumetric pipette, Volumetric flask. they are SingleMarked now available. it is based on list of JIS R 3505.
if you Use Subclass of Single Marked Glassware. The instance will return uncertain quantity of quantities.
## Volumetric Pipette
Volumetric Pipette class supports almost operators. but reverse division operator is disabled.Because Pipette is to pick solution up. Not for diffusion.

## Volumetric flask
Volumetric Flask class supports almost operators. but reverse multiple operator returns uncertain quantity which have double uncertain.thus JIS standard define so.

# Multiple Marked Glassware
Volumetric Cylinder, Measure pipette, Gellbert and Bubcock oil guage are here. on goiing now.

