import numpy as np
import menuTools as mt
##########
# all finger close = 0
# all finger open = 1
# işaret parmağı = 2
# işaret parmağı ve orta = 3
# işaret parmağıyla birlikte yandaki ikili = 4
# baş parmak açık = 5
# baş parmak ve işaret parmağı = 6
# baş parmak ve işaret parmağı ve orta parmak = 7
# baş parmak dışında hepsi
##########

###
#not : bir ara sağ ve sol ele göre ayarlanması gerekiyor
###
class fingerTools():
    def fingersMode(fingers):
        fn = np.array(fingers)
        fn = fn.astype(np.bool)
        p1,p2,p3,p4,p5=fn.tolist()  

        #bu kısmı ters çalıştığı düzeltme yapmak için değilledik
        if mt._settings.isFlipMode:
            p1 = not p1
        if not p1 and not p2 and not p3 and not p4 and not p5:
            return 0
        elif p1 and p2 and p3 and p4 and p5:
            return 1
        elif not p1 and p2 and not p3 and not p4 and not p5:
            return 2
        elif not p1 and p2 and p3 and not p4 and not p5:
            return 3
        elif not p1 and p2 and p3 and p4 and not p5:
            return 4
        elif p1 and not p2 and not p3 and not p4 and not p5:
            return 5
        elif p1 and p2 and not p3 and not p4 and not p5:
            return 6
        elif p1 and p2 and p3 and not p4 and not p5:
            return 7
        elif not p1 and p2 and p3 and p4 and p5:
            return 8
        else:
            return -1