import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

bps = 9600.
fs = 96000.
spb = int(fs/bps)

x = np.array([-0.30095288157463074, -0.20654478669166565, 0.021702393889427185, -0.10304533690214157, 0.06360501796007156, -0.02583719976246357, -0.07634343951940536, 0.02434881404042244, -0.028336962684988976, -0.007157610263675451, -0.05542263016104698, -0.07013727724552155, 0.06646080315113068, 0.03562410920858383, -0.10637535899877548, -0.03892992064356804, -0.004845966584980488, -0.03404802083969116, -0.019582873210310936, 0.030032135546207428, -0.016225947067141533, -0.0512983575463295, -0.014268919825553894, -0.08857374638319016, -0.04086952656507492, -0.00034503359347581863, -0.08496744185686111, 0.05857842415571213, 0.033198580145835876, -0.04101676121354103, -0.042600683867931366, -0.060997381806373596, -0.0046012066304683685, 0.004521692171692848, -0.05366130173206329, -0.09710844606161118, 0.01399972289800644, 0.06484344601631165, -0.07478799670934677, -0.0220356248319149, -0.03634532168507576, -0.01977938413619995, -0.00594255980104208, -0.07189434766769409, 0.04685954004526138, -0.08934347331523895, 0.011226877570152283, -0.05000850930809975, -0.10083786398172379, 0.1022515594959259, -0.053177978843450546, -0.07311339676380157, 0.034520599991083145, -0.021654698997735977, -0.04279668629169464, -0.007245668675750494, -0.008217120543122292, -0.08492991328239441, -0.06706900894641876, 0.08938390016555786, -0.0015153633430600166, -0.0631534606218338, -0.052910421043634415, -0.03426001965999603, -0.010893336497247219, -0.03692087158560753, 0.05822833627462387, -0.09786705672740936, -0.017992418259382248, 0.025774609297513962, -0.09973233938217163, 0.041038960218429565, -0.045768000185489655, -0.04050879925489426, -0.004272785969078541, -0.04817773029208183, 0.005247987806797028, -0.005656796507537365, -0.06579157710075378, 0.04455297812819481, 0.030813563615083694, -0.8698623776435852, -1.4944192171096802, -1.4047666788101196, -1.3831454515457153, -1.3531862497329712, -1.3390440940856934, -1.3240728378295898, -1.4826178550720215, -1.2697594165802002, -1.441036343574524, -1.395497441291809, -1.3770081996917725, -1.311607837677002, -1.462432861328125, -1.3760720491409302, -1.3322621583938599, -1.3167911767959595, -1.3432201147079468, -1.4932589530944824, -1.3785735368728638, 0.2789207994937897, 1.3761119842529297, 1.4144132137298584, 1.2306922674179077, 1.339141607284546, 1.3284169435501099, 1.3547518253326416, 1.3526602983474731, 1.2768391370773315, 1.3363163471221924, -0.2862396836280823, -1.3798599243164062, -1.4035297632217407, -1.398131012916565, -1.3336788415908813, -1.3995287418365479, -1.347113847732544, -1.3896687030792236, -1.44718337059021, -1.3426134586334229, 0.11503426730632782, 1.5376564264297485, 1.3249764442443848, 1.3777726888656616, 1.2468886375427246, 1.2959603071212769, 1.4440125226974487, 1.269968867301941, 1.3639650344848633, 1.3509140014648438, -0.24683158099651337, -1.4666191339492798, -1.380910038948059, -1.431640625, -1.3417526483535767, -1.386515736579895, -1.3551911115646362, -1.4082485437393188, -1.3672698736190796, -1.3803709745407104, 0.1945277899503708, 1.392751693725586, 1.3124536275863647, 1.41947603225708, 1.2141577005386353, 1.3303240537643433, 1.3760370016098022, 1.2966383695602417, 1.427303671836853, 1.3640644550323486, -0.1793740689754486, -1.5376564264297485, -1.405295491218567, -1.3645000457763672, -1.3402303457260132, -1.353653907775879, -1.4305408000946045, -1.352744460105896, -1.424013376235962, -1.369695782661438, 0.18950214982032776, 1.4028693437576294, 1.360385537147522, 1.3233788013458252, 1.2994987964630127, 1.2872036695480347, 1.362065076828003, 1.2914820909500122, 1.360081672668457, 1.3875638246536255, -0.25238391757011414, -1.4271607398986816, -1.4622002840042114, -1.3558743000030518, -1.3406479358673096, -1.3304762840270996, -1.3581780195236206, -1.3667000532150269, -1.4415812492370605, -1.399664044380188, 0.13661958277225494, 1.436377763748169, 1.3561615943908691, 1.3869962692260742, 1.2527331113815308, 1.312978982925415, 1.2940075397491455, 1.3583227396011353, 1.3180444240570068, 1.350175380706787, -0.13668566942214966, -1.4408336877822876, -1.3880493640899658, -1.477931022644043, -1.2965296506881714, -1.3706446886062622, -1.3998517990112305, -1.3906296491622925, -1.3991113901138306, -1.3920221328735352, 0.16568857431411743, 1.3705204725265503, 1.3752962350845337, 1.2605838775634766, 1.4003710746765137, 1.278555989265442, 1.4265108108520508, 1.2966707944869995, 1.2875950336456299, 1.3672939538955688, -0.13100293278694153, -1.4807178974151611, -1.353448748588562, -1.378692865371704, -1.4271173477172852, -1.3390694856643677, -1.4513260126113892, -1.2365213632583618, -1.480265736579895, -1.3862756490707397, 0.11971142888069153, 1.4011309146881104, 1.4134327173233032, 1.264750599861145, 1.3124626874923706, 1.3562443256378174, 1.2526029348373413, 1.365531325340271, 1.3458856344223022, 1.3075436353683472, -0.0895446315407753, -1.440123200416565, -1.3671122789382935, -1.439955234527588, -1.3361855745315552, -1.3456134796142578, -1.3879722356796265, -1.4451398849487305, -1.3854343891143799, -1.3297380208969116, 0.03525592386722565, 1.3921382427215576, 1.46828031539917, 1.1985591650009155, 1.3512293100357056, 1.2757680416107178, 1.3899378776550293, 1.3530328273773193, 1.3289638757705688, 1.4164470434188843, -0.13625097274780273, -1.5120937824249268, -1.3968051671981812, -1.437421441078186, -1.2957087755203247, -1.4041632413864136, -1.3329330682754517, -1.3643863201141357, -1.3992213010787964, -1.3917608261108398, 0.09252555668354034, 1.3347443342208862, 1.4248970746994019, 1.1935474872589111, 1.4531121253967285, 1.2377243041992188, 1.3516050577163696, 1.2906957864761353, 1.4142321348190308, 1.360840082168579, -0.15559826791286469, -1.3789796829223633, -1.447914481163025, -1.320439100265503, -1.408052682876587, -1.4004074335098267, -1.2969343662261963, -1.4249399900436401, -1.4011651277542114, -1.4384186267852783, 0.0664161816239357, 1.3600908517837524, 1.4177885055541992, 1.305614948272705, 1.3215090036392212, 1.3712520599365234, 1.3115953207015991, 1.3268927335739136, 1.4229024648666382, 1.2564359903335571, -0.04911836236715317, -1.4590469598770142, -1.4565359354019165, -1.3386025428771973, -1.3934983015060425, -1.2350050210952759, -1.4221328496932983, -1.3859233856201172, -1.406951665878296, -1.3589075803756714, -0.0945664569735527, 1.3692775964736938, 1.3527852296829224, 1.4084471464157104, 1.337219476699829, 1.2806464433670044, 1.3014920949935913, 1.3383482694625854, 1.387467861175537, 1.3701914548873901, -0.1321321427822113, -1.4002811908721924, -1.4366499185562134, -1.3936569690704346, -1.3456976413726807, -1.3835475444793701, -1.3220692873001099, -1.3680967092514038, -1.3663276433944702, -1.3892751932144165, 0.0016889013350009918, 1.3632522821426392, 1.3547276258468628, 1.3171933889389038, 1.2984098196029663, 1.3969882726669312, 1.2848669290542603, 1.2883106470108032, 1.400128722190857, 1.275071382522583, -0.003993158228695393, -1.4141279458999634, -1.3929345607757568, -1.4126181602478027, -1.352364420890808, -1.3443613052368164, -1.405802845954895, -1.347511887550354, -1.4188777208328247, -1.4562257528305054, -0.00453697144985199, 1.4693557024002075, 1.334230899810791, 1.298467993736267, 1.3146973848342896, 1.3331111669540405, 1.3419991731643677, 1.318261742591858, 1.3407930135726929, 1.4348819255828857, -0.107892706990242, -1.3608148097991943, -1.5161967277526855, -1.1785494089126587, -1.4866219758987427, -1.348974585533142, -1.395828127861023, -1.3607604503631592, -1.3863428831100464, -1.4263705015182495, -0.03712692856788635, 1.4141602516174316, 1.3600486516952515, 1.3070381879806519, 1.2823740243911743, 1.3745650053024292, 1.2755662202835083, 1.3082777261734009, 1.3852497339248657, 1.2513841390609741, 0.06618956476449966, -1.4049879312515259, -1.3166450262069702, -1.426343560218811, -1.3629919290542603, -1.3849347829818726, -1.4053632020950317, -1.319746732711792, -1.4498872756958008, -1.3876817226409912, -0.08339066058397293, 1.3977692127227783, 1.3557369709014893, 1.3871113061904907, 1.2781486511230469, 1.3350064754486084, 1.2596943378448486, 1.3816150426864624, 1.313632845878601, 1.4376188516616821, -0.019124262034893036, -1.4260790348052979, -1.3639675378799438, -1.4611942768096924, -1.3358652591705322, -1.3493402004241943, -1.380731225013733, -1.3525986671447754, -1.4363256692886353, -1.426377534866333, -0.08928397297859192, 1.4635776281356812, 1.274613857269287, 1.475824236869812, 1.2357720136642456, 1.3430346250534058, 1.35153067111969, 1.2488360404968262, 1.3897883892059326, 1.440022587776184, 0.00874791108071804, -1.4433951377868652, -1.4602011442184448, -1.3204654455184937, -1.4642595052719116, -1.2629351615905762, -1.4262794256210327, -1.4214885234832764, -1.3266496658325195, -1.4601519107818604, -0.09468892216682434, 1.4166868925094604, 1.3653804063796997, 1.2833787202835083, 1.320249080657959, 1.3166989088058472, 1.3299987316131592, 1.3361481428146362, 1.3249878883361816, 1.354517936706543, 1.317958950996399, 1.2566591501235962, 1.3688596487045288, 1.348446011543274, 1.3999607563018799, 1.2986009120941162, 1.2132182121276855, 1.3210639953613281, 1.3624500036239624, 1.349535346031189, 1.3481632471084595, 1.3317384719848633, 1.3418118953704834, 1.2539318799972534, 1.361419439315796, 1.3004425764083862, 1.37758469581604, 1.3005627393722534, 1.3350132703781128, 1.372886300086975, 1.2692700624465942, 1.32980215549469, 1.3125896453857422, 1.3974398374557495, 1.344111680984497, 1.3033604621887207, 1.3126028776168823, 1.2734791040420532, 1.400044560432434, 1.3286347389221191, 1.2790195941925049, 1.332000494003296, 1.3255046606063843, 1.327012300491333, 1.3329885005950928, 1.3524657487869263, 1.26179039478302, 1.3935071229934692, 1.3708781003952026, 1.333321213722229, 0.12718279659748077, -1.3660379648208618, -1.4668024778366089, -1.460205078125, -1.3038661479949951, -1.4029204845428467, -1.268654227256775, -1.439613699913025, -1.450793981552124, -1.3038944005966187, -0.19856376945972443, 1.277695894241333, 1.40603506565094, 1.3192239999771118, 1.344957709312439, 1.3512736558914185, 1.3022074699401855, 1.3102293014526367, 1.3821686506271362, 1.3043237924575806, 1.345833420753479, 1.3288766145706177, 1.3314632177352905, 1.2661904096603394, 1.392994999885559, 1.2683194875717163, 1.3610577583312988, 1.313122272491455, 1.4143292903900146, 1.3374478816986084, 0.10443417727947235, -1.4458240270614624, -1.3528095483779907, -1.4374603033065796, -1.3358491659164429, -1.4022810459136963, -1.3359442949295044, -1.3943700790405273, -1.3240805864334106, -1.4960472583770752, -0.18624025583267212, 1.314848780632019, 1.3939272165298462, 1.2556275129318237, 1.4067376852035522, 1.2791898250579834, 1.3295137882232666, 1.3639872074127197, 1.2687052488327026, 1.3853964805603027, 1.256083607673645, 1.4199577569961548, 1.3196991682052612, 1.3184490203857422, 1.3644896745681763, 1.2500935792922974, 1.3718541860580444, 1.3081103563308716, 1.3435114622116089, 1.3171409368515015, 1.390051245689392, 1.2937654256820679, 1.2921463251113892, 1.351633906364441, 1.332673192024231, 1.3205492496490479, 1.2707080841064453, 1.2851659059524536, 1.3759607076644897, 1.369673728942871, 0.25830864906311035, -1.4535335302352905, -1.4392224550247192, -1.3353946208953857, -1.3339111804962158, -1.428269386291504, -1.327696681022644, -1.4066449403762817, -1.3479470014572144, -1.3633699417114258, -1.3803763389587402, -1.375892162322998, -1.3828507661819458, -1.3910441398620605, -1.360538125038147, -1.3928354978561401, -1.3129609823226929, -1.3873275518417358, -1.4313254356384277, -1.3796981573104858, -0.25572681427001953, 1.3730388879776, 1.3301489353179932, 1.3597692251205444, 1.3095898628234863, 1.287269115447998, 1.3861242532730103, 1.3291813135147095, 1.257171392440796, 1.4462144374847412, 0.1707909256219864, -1.3953665494918823, -1.3758450746536255, -1.38936448097229, -1.440086007118225, -1.321021318435669, -1.3672642707824707, -1.2805947065353394, -1.4416409730911255, -1.4870457649230957, -0.25900495052337646, 1.3615002632141113, 1.36933434009552, 1.3237470388412476, 1.3139928579330444, 1.3156214952468872, 1.2905136346817017, 1.3225035667419434, 1.4166368246078491, 1.381381869316101, 0.2750718593597412, -1.4742777347564697, -1.3134348392486572, -1.454489827156067, -1.3280025720596313, -1.3417598009109497, -1.4415154457092285, -1.3231171369552612, -1.4738260507583618, -1.3472539186477661, -0.34078097343444824, 1.3311543464660645, 1.3913744688034058, 1.326029896736145, 1.364685297012329, 1.317207932472229, 1.3302782773971558, 1.2663942575454712, 1.3958756923675537, 1.3251724243164062, 1.3467587232589722, 1.260955572128296, 1.3838435411453247, 1.2958095073699951, 1.3039088249206543, 1.346146821975708, 1.3444424867630005, 1.2903028726577759, 1.3684660196304321, 1.4191051721572876, 0.1575705111026764, -1.382712721824646, -1.3798047304153442, -1.3563671112060547, -1.4044809341430664, -1.2954427003860474, -1.3915845155715942, -1.3818964958190918, -1.4576787948608398, -1.4095524549484253, -0.2936456799507141, 1.2953675985336304, 1.433201551437378, 1.2827847003936768, 1.3341470956802368, 1.2964388132095337, 1.3524280786514282, 1.3178532123565674, 1.4174472093582153, 1.2895797491073608, 0.26231154799461365, -1.4288345575332642, -1.3971515893936157, -1.3385521173477173, -1.3663222789764404, -1.3443492650985718, -1.325692057609558, -1.3970445394515991, -1.4387192726135254, -1.4959723949432373, -0.2926428020000458, 1.353423833847046, 1.4108988046646118, 1.3496663570404053, 1.3008652925491333, 1.3113164901733398, 1.2804185152053833, 1.365047812461853, 1.3412004709243774, 1.3406355381011963, 1.3368748426437378, 1.2815515995025635, 1.3284715414047241, 1.3541704416275024, 1.353793740272522, 1.3283857107162476, 1.348694920539856, 1.2864038944244385, 1.3017610311508179, 1.2903436422348022, 1.3460884094238281, 1.3000829219818115, 1.2898319959640503, 1.4207615852355957, 1.2850595712661743, 1.3483601808547974, 1.3612456321716309, 1.2727612257003784, 1.315804123878479, 1.3368059396743774, 1.3588474988937378, 1.2461870908737183, 1.3802939653396606, 1.3787003755569458, 1.209998607635498, 1.4356333017349243, 1.3656535148620605, 1.286035180091858, 1.298998236656189, 1.3375779390335083, 1.2992373704910278, 1.3217220306396484, 1.3489452600479126, 1.3499058485031128, 1.30501389503479, 1.4081050157546997, 1.3119256496429443, 1.260117769241333, 1.3417531251907349, 1.4058793783187866, 0.3246672749519348, -1.4233993291854858, -1.3649368286132812, -1.3567086458206177, -1.4412568807601929, -1.3060716390609741, -1.3483513593673706, -1.3812096118927002, -1.4442945718765259, -1.39971923828125, -0.3930930197238922, 1.3562623262405396, 1.3465611934661865, 1.3217326402664185, 1.2693547010421753, 1.3253190517425537, 1.3555525541305542, 1.3777811527252197, 1.3188658952713013, 1.266809105873108, 1.3409228324890137, 1.3138619661331177, 1.2940720319747925, 1.403294563293457, 1.3384839296340942, 1.265234112739563, 1.3079153299331665, 1.309415578842163, 1.343770980834961, 1.3361374139785767, 1.3659985065460205, 1.3415565490722656, 1.2831778526306152, 1.3938440084457397, 1.3063703775405884, 1.2720272541046143, 1.3267039060592651, 1.341158390045166, 1.3715015649795532, 1.3483926057815552, 1.3654948472976685, 1.325856328010559, 1.2595406770706177, 1.3572020530700684, 1.2182286977767944, 1.4130496978759766, 1.2868283987045288, 1.2959908246994019, 1.3596190214157104, 1.3229832649230957, 1.2703051567077637, 1.3500405550003052, 1.3983054161071777, 1.3487416505813599, 1.2992953062057495, 1.2947068214416504, 1.4107111692428589, 1.241126537322998, 1.3996760845184326, 1.2630374431610107, 1.4148023128509521, 1.2893061637878418, 1.3065311908721924, 1.297828197479248, 1.264846920967102, 1.4018884897232056, 1.304701328277588, 1.3042519092559814, 1.3655829429626465, 1.3202458620071411, 1.324267029762268, 1.3723101615905762, 1.2958189249038696, 1.3079913854599, 1.347877025604248, 1.329264760017395, 1.2856332063674927, 1.3205512762069702, 1.3505839109420776, 1.3639479875564575, 0.4452156126499176, -1.3470802307128906, -1.4215004444122314, -1.4516019821166992, -1.3629088401794434, -1.323126196861267, -1.3134722709655762, -1.3975117206573486, -1.441519856452942, -1.4048300981521606, -0.48403415083885193, 1.3565046787261963, 1.247164249420166, 1.4167098999023438, 1.2936551570892334, 1.3800183534622192, 1.3226813077926636, 1.3036631345748901, 1.3368809223175049, 1.3587825298309326, 1.2896528244018555, 1.4136574268341064, 1.2886401414871216, 1.3558169603347778, 1.2815107107162476, 1.2789146900177002, 1.4219642877578735, 1.2161879539489746, 1.373408317565918, 1.3364862203598022, 0.4666644036769867, -1.3836971521377563, -1.3817307949066162, -1.3617602586746216, -1.3807027339935303, -1.2864248752593994, -1.430040717124939, -1.3091965913772583, -1.4395081996917725, -1.4775511026382446, -0.4696722626686096, 1.3482956886291504, 1.3129416704177856, 1.3599817752838135, 1.2829002141952515, 1.37870454788208, 1.2476099729537964, 1.3375701904296875, 1.433127522468567, 1.3358412981033325, 0.40825843811035156, -1.3213123083114624, -1.431848406791687, -1.3878904581069946, -1.318580985069275, -1.37551748752594, -1.3145719766616821, -1.4077426195144653, -1.4202649593353271, -1.368129014968872, -1.4364913702011108, -1.3093253374099731, -1.394716501235962, -1.3676220178604126, -1.3647526502609253, -1.328304409980774, -1.369523048400879, -1.4022067785263062, -1.4260376691818237, -1.372122049331665, -1.3678785562515259, -1.373920202255249, -1.323525071144104, -1.4374126195907593, -1.3540024757385254, -1.3732620477676392, -1.2573193311691284, -1.4622541666030884, -1.431896686553955, -1.3632323741912842, -1.3319518566131592, -1.3606449365615845, -1.4047342538833618, -1.3951102495193481, -1.2869250774383545, -1.415482759475708, -1.3646807670593262, -1.3606222867965698, -1.4539299011230469, -1.3079038858413696, -1.30514395236969, -1.4363207817077637, -1.3302713632583618, -1.4092010259628296, -1.3223891258239746, -1.4328328371047974, -1.3522768020629883, -1.408307671546936, -1.3963514566421509, -1.3055343627929688, -1.4276762008666992, -1.3374923467636108, -1.3725104331970215, -1.4283487796783447, -1.3610776662826538, -1.377489447593689, -1.3777209520339966, -1.2641412019729614, -1.5432047843933105, -1.28490149974823, -0.6290907859802246, 1.366500735282898, 1.2445189952850342, 1.359621524810791, 1.3736224174499512, 1.2854578495025635, 1.3505079746246338, 1.3913742303848267, 1.2392754554748535, 1.3680849075317383, 1.2386304140090942, 1.3430644273757935, 1.3670228719711304, 1.284075140953064, 1.3629189729690552, 1.3349934816360474, 1.3057752847671509, 1.2602146863937378, 1.4538917541503906, 1.3728411197662354, 0.5569954514503479, -1.3669633865356445, -1.4194689989089966, -1.3908005952835083, -1.3830626010894775, -1.360907793045044, -1.3262519836425781, -1.428673505783081, -1.3466469049453735, -1.3674771785736084, -1.3626652956008911, -1.4108710289001465, -1.3698102235794067, -1.3944034576416016, -1.3558562994003296, -1.3691455125808716, -1.3407694101333618, -1.3787654638290405, -1.5197330713272095, -1.3477824926376343, -0.5923928022384644, 1.282692313194275, 1.2836047410964966, 1.3831599950790405, 1.3894778490066528, 1.278899073600769, 1.3008631467819214, 1.3675957918167114, 1.2945410013198853, 1.3145993947982788, 1.3110116720199585, 1.37941312789917, 1.319901943206787, 1.3622453212738037, 1.3127654790878296, 1.3222806453704834, 1.3407167196273804, 1.3523467779159546, 1.2888462543487549, 1.339486837387085, 1.2612367868423462, 1.3283847570419312, 1.2802718877792358, 1.4253071546554565, 1.297208547592163, 1.3821419477462769, 1.2777223587036133, 1.2516100406646729, 1.4009904861450195, 1.4371362924575806, 0.5403998494148254, -1.4461946487426758, -1.2223055362701416, -1.452377438545227, -1.3261033296585083, -1.3965892791748047, -1.298096776008606, -1.3380376100540161, -1.5134532451629639, -1.4651498794555664, -0.580889105796814, 1.3265419006347656, 1.2687759399414062, 1.3646985292434692, 1.340512990951538, 1.2967349290847778, 1.3446462154388428, 1.3145488500595093, 1.3646798133850098, 1.3300913572311401, 0.6702108979225159, -1.352646827697754, -1.3763388395309448, -1.3877581357955933, -1.4630953073501587, -1.3039854764938354, -1.3987689018249512, -1.3214772939682007, -1.4707006216049194, -1.3587915897369385, -0.6819310784339905, 1.3616987466812134, 1.2222844362258911, 1.4315135478973389, 1.2801358699798584, 1.32375967502594, 1.2869387865066528, 1.3640711307525635, 1.3818162679672241, 1.3953241109848022, 0.5576450228691101, -1.341654896736145, -1.356630563735962, -1.3790786266326904, -1.3465503454208374, -1.426804542541504, -1.37490713596344, -1.3514090776443481, -1.3619276285171509, -1.320090651512146, -1.4726903438568115, -1.3597913980484009, -1.3395261764526367, -1.384675145149231, -1.3567739725112915, -1.3546122312545776, -1.375363826751709, -1.400107502937317, -1.39663827419281, -1.3423264026641846, -1.3823567628860474, -1.3779815435409546, -1.396389126777649, -1.3761526346206665, -1.3457562923431396, -1.3814774751663208, -1.3832448720932007, -1.2862536907196045, -1.4569118022918701, -1.4291411638259888, -0.6599506735801697, 1.2058743238449097, 1.303317904472351, 1.3722985982894897, 1.33180570602417, 1.2603867053985596, 1.4205950498580933, 1.3107613325119019, 1.2913542985916138, 1.3365654945373535, 1.340341329574585, 1.364296555519104, 1.316952109336853, 1.2610775232315063, 1.304614782333374, 1.3928941488265991, 1.2668217420578003, 1.367909550666809, 1.3308569192886353, 1.3199594020843506, 0.7030957937240601, -1.2576850652694702, -1.3353655338287354, -1.4012047052383423, -1.4141217470169067, -1.354278564453125, -1.4349312782287598, -1.3558928966522217, -1.3426947593688965, -1.3181086778640747, -1.4431008100509644, -1.3295873403549194, -1.3531028032302856, -1.4367601871490479, -1.3035825490951538, -1.4554017782211304, -1.3136224746704102, -1.3965941667556763, -1.382681131362915, -1.3861716985702515, -1.438442587852478, -1.3259532451629639, -1.3770664930343628, -1.3430538177490234, -1.441964030265808, -1.353659987449646, -1.3069614171981812, -1.3882111310958862, -1.328626036643982, -1.4225462675094604, -1.4334118366241455, -1.323687195777893, -1.3973803520202637, -1.26850163936615, -1.4946240186691284, -1.257099986076355, -1.4416319131851196, -1.338585376739502, -1.400553822517395, -1.413073182106018, -1.3962266445159912, -1.2759469747543335, -1.3724933862686157, -1.4155442714691162, -1.3875473737716675, -1.386123538017273, -1.3913383483886719, -1.374904990196228, -1.3235008716583252, -1.3820544481277466, -1.4119272232055664, -1.3415274620056152, -1.3906391859054565, -1.3512495756149292, -1.3336750268936157, -1.4752259254455566, -1.3039919137954712, -1.3982523679733276, -1.328737735748291, -1.4108022451400757, -1.4039192199707031, -1.3341503143310547, -1.3357268571853638, -1.381325602531433, -1.4379805326461792, -1.3484212160110474, -1.3946503400802612, -1.3432461023330688, -1.376147747039795, -1.3961769342422485, -1.3604106903076172, -1.3737688064575195, -1.3891847133636475, -1.3534082174301147, -1.3744629621505737, -1.3455140590667725, -1.4606478214263916, -1.3051366806030273, -1.4739528894424438, -1.3685096502304077, -0.7272152304649353, 1.226601481437683, 1.298977017402649, 1.3208156824111938, 1.3647377490997314, 1.2679879665374756, 1.2442138195037842, 1.407793402671814, 1.3085702657699585, 1.3648203611373901, 0.7651777863502502, -1.2130132913589478, -1.3370331525802612, -1.4356586933135986, -1.3898252248764038, -1.3279247283935547, -1.4204144477844238, -1.342980146408081, -1.406945824623108, -1.4174482822418213, -1.284149169921875, -1.3948028087615967, -1.422250747680664, -1.2624080181121826, -1.077698826789856, -0.8233909010887146, -2.4959259033203125, -2.4299569129943848, 0.14963822066783905, 3.244119644165039, 1.9710850715637207, -1.1155683994293213, -3.073383331298828, -0.7826124429702759, -3.1111717224121094, -5.762369632720947, -6.230910301208496, -4.00698184967041, -5.549553394317627, -8.172747611999512, -7.466009616851807, -7.399235725402832, -7.767506122589111, -5.797520160675049, -8.104083061218262, -8.492247581481934, -5.890746116638184, -3.7522401809692383, -4.504191875457764, -7.21615743637085, -6.8708109855651855, -4.949604511260986, -6.811751842498779, -7.441495895385742, -6.084049701690674, -3.993915557861328, -2.0863256454467773, -0.7819867730140686, -2.912745952606201, -2.268040180206299, 0.30792444944381714, -1.1948291063308716, 0.7846595048904419, 2.9816603660583496, 3.14431095123291, 1.913011908531189, -0.5406743288040161, 0.39023688435554504, -1.9349758625030518])

def demodulate(input, sps):
    b = np.ones((int(np.floor(spb/2)*2),))
    b[int(len(b)/2):] = -1
    b = b / len(b)
    a = 1.
    xf = signal.lfilter(b, a, input)
    # Hysteresis detector
    hys = np.zeros(xf.size)
    hys_pos = xf>0.5
    hys_neg = xf<-0.5
    state = 0
    n = 0
    for up, dn in zip(hys_pos, hys_neg):
        if up:
            hys[n] = 1
        elif dn:
            hys[n] = -1
        elif n>0:
            hys[n] = hys[n-1]
        n += 1
    # Correlate to sync
    # sync = np.concatenate((np.ones((spb,)), -1*np.ones((spb,))))
    # sync = np.concatenate((sync, sync, sync, sync, sync, sync, sync, sync, sync, sync, sync, sync, sync, sync, sync))
    # sync = np.concatenate((-1*np.ones((2*spb,)), sync))
    # sync = np.concatenate((sync, np.ones((2*spb,))))
    # xc = np.correlate(hys, sync)
    start = np.argmax(np.abs(hys))
    bits = hys[start+1::spb]
    return (bits[:107], start)


bits, start = demodulate(x, spb)

L = len(x)
t = np.arange(0.0, L, 1)/fs
tb = (np.arange(0.0, len(bits), 1) + start/spb) / bps
fig, ax = plt.subplots()
ax.plot(t, x)
# ax.plot(t, xf)
# ax.plot(t, hys)
ax.stem(tb, bits>0)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='bits')
ax.grid()
plt.show()