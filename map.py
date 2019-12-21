from tile import *

ref_w = Ground.width
ref_h = Ground.height
map = [
    [
        [
            Cloud(x=150, y=100),
            Fence(x=70, y=ref_w * 7 + 20)
        ],

        [
            Ground(x=ref_w * 0, y=ref_h * 8),
            Ground(x=ref_w, y=ref_h * 8),
            Bonus(x=ref_w * 2, y=ref_h * 6 - 30),
            Bridge(x=ref_w * 2, y=ref_h * 8),
            Bridge(x=ref_w * 3, y=ref_h * 8),
            GoldCoin(x=ref_w * 5, y=ref_h * 7),
            Spikes(x=ref_w * 4, y=ref_h * 8 + 20),
            Plank(x=int(ref_w * 4.5),y=ref_h*7+35),
            Spikes(x=ref_w * 5, y=ref_h * 8 + 20),
            GoldCoin(x=ref_w * 1, y=ref_h * 7),
            Bridge(x=ref_w * 6, y=ref_h * 8),
            Bridge(x=ref_w * 7, y=ref_h * 8),
            Bridge(x=ref_w * 8, y=ref_h * 8)
        ],

        [
            Grass(x=0, y=ref_w * 7 + 30)
        ]
    ],
    [
        [
            Fence(x=ref_w * 5,y=ref_h*7+20)
        ],
        [
            Bridge(x=ref_w * 0, y=ref_h * 8),
            Bridge(x=ref_w * 1, y=ref_h * 8),

            Plank(x=int(ref_w * 2.5), y=int(ref_h * 7.5)),
            Plank(x=int(ref_w * 3.5), y=int(ref_h * 6.5)),
            Water(x=ref_w * 3, y=ref_h * 8),
            Water(x=ref_w * 4, y=ref_h * 8),
            Plank(x=int(ref_w * 4.5), y=int(ref_h * 5.5)),
            Ground(x=ref_w * 5, y=ref_h * 8),
            KeyRed(x=ref_w * 6, y=ref_h * 7),
            Ground(x=ref_w * 6, y=ref_h * 8),
            Ground(x=ref_w * 7, y=ref_h * 8),
            Ground(x=ref_w * 8, y=ref_h * 8),
        ],
        [

        ]
    ],
    [
        [

        ],
        [
            Ground(x=ref_w * 0, y=ref_h * 8),
            Ground(x=ref_w * 1, y=ref_h * 8),
            Ground(x=ref_w * 2, y=ref_h * 8),
            Ground(x=ref_w * 3, y=ref_h * 8),
            Ground(x=ref_w * 4, y=ref_h * 8),
            HillLong(x=ref_w * 5, y=ref_h * 7)
        ],
        [

        ]
    ]
]
