from pylab import *
from numpy import *

down = '''
54
166
279
357
396
469
531
582
650
793
931
1081
1191
1285
1372
1467
1666
1841
1933
2042
2113
2240
2356
2543
2709
2867
2997
3150
3344
3735
4076
4348
4672
5074
5262
5456
5769
6025
6307
6669
7042
7396
7828
8179
8484
8970
9309
9579
9833
10300
10684
11023
11351
11807
12089
12427
12706
13038
13349
13751
14103
14806
15229
15579
15922
16275
16648
16955
17347
17739
18215
18629
18941
19264
19496
19828
20250
20679
21078
21436
21848
22238
22588
22953
23197
23807
24322
25800
26139
26463
26791
27093
27427
27734
28131
28630
28973
29412
29769
30226
30614
31014
31376
31795
32084
32525
33146
33529
34007
34621
35156
35523
35956
36306
36613
36931
37328
37850
38385
38798
39095
39667
40378
40962
41495
41900
42204
42429
42720
43027
43457
43707
43906
44236
44495
44792
45141
45425
45663
45948
46094
46395
46655
46915
47124
47395
47656
47880
48130
48398
48554
48807
49043
49216
49406
49567
49716
49842
49984
50231
50494
50694
50966
'''

down = map(int,down.split())
ind = arange(len(down))
width=0.75

clf()
p1 = bar(ind,down,width)
ylabel('Downloads')
xticks(ind[::12]+width/2,
       ('6/06','6/07','6/08','6/09','6/10','6/11','6/12','6/13','6/14','6/15','6/16',
        '6/17','6/18','6/19'))
title('Cumulative Downloads')
#grid(True)

#show()
savefig('junk_py.eps')
