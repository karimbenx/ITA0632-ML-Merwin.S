Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

== RESTART: C:/Users/Merwin S/AppData/Local/Programs/Python/Python311/ml 3.py ==
Training Data:
   No     Shape   Size  Color    Surface Thickeness Target Concept
0   1  Circular  Large  Light     Smooth      Thick   Malignant(+)
1   2  Circular  Large  Light  Irregular      Thick   Malignant(+)
2   3      Oval  Large   Dark     Smooth       Thin     Beningn(-)
3   4      Oval  Large  Light  Irregular      Thick   Malignant(+)

Most specific hypothesis using FIND-S: ['?', '?', 'Large', 'Light', '?', 'Thick']

Instance: [1, 'Circular', 'Large', 'Light', 'Smooth', 'Thick', 'Malignant(+)']
Specific Hypothesis: [1, 'Circular', 'Large', 'Light', 'Smooth', 'Thick']
General Hypotheses:
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object

Instance: [2, 'Circular', 'Large', 'Light', 'Irregular', 'Thick', 'Malignant(+)']
Specific Hypothesis: ['?', 'Circular', 'Large', 'Light', '?', 'Thick']
General Hypotheses:
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object

Instance: [3, 'Oval', 'Large', 'Dark', 'Smooth', 'Thin', 'Beningn(-)']
Specific Hypothesis: ['?', 'Circular', 'Large', 'Light', '?', 'Thick']
General Hypotheses:
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object

Instance: [4, 'Oval', 'Large', 'Light', 'Irregular', 'Thick', 'Malignant(+)']
Specific Hypothesis: ['?', '?', 'Large', 'Light', '?', 'Thick']
General Hypotheses:
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object

Most specific hypothesis using CE: ['?', '?', 'Large', 'Light', '?', 'Thick']
General hypotheses using CE:
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
0    ?
1    ?
2    ?
3    ?
4    ?
5    ?
dtype: object
