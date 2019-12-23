from tile import *
class Map:

    def __init__(self):


        ref_w = Ground.width
        ref_h = Ground.height
        self.map = [
            [
                [
                    BackgroundForest(0,0),
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

        self.region = self.map[0]
        self.region_count = 0

    def region_changes(self, player):

        if player._x > 600 - player.width and \
                self.region_count < len(self.map) - 1:
            player.min_pos_player()
            self.region_count += 1
            self.region = self.map[self.region_count]

        if player._x < 0 and self.region_count > 0:
            player.max_pos_player()
            self.region_count -= 1
            self.region = self.map[self.region_count]

        return player
