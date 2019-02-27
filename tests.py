from main import Solution

class TestClass(object):

    def setup_method(self, method):
        self.solution = Solution()
    
    def test_one(self):
        
        test1 = """shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en yco
        ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw
        wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpe
        igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh
        ihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd
        lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild
        rfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql"""

        sorted_ = """sqflo spqinedf sfoqmd syejrqd shoce srdueqhgiy sionpux xclpedqmi xlmnfqry xrpmyenq xrdng ocxfsjdng oewgjfr ojxfqhernm cop coj cmfur cwj cpqmxj chwjlg cejfugn qx qplfjnwidg
        qhmoixw ql qdrulxogji qinhmjul qinexwo qihmu ncsepfl nmodwsqijh nwcrus nfwh nj ng ms mw mwd
        mlceo mjxdqfrnlg wxflpdn whc wjuln podciy pq py phfer prfmjicud pdoymnwxei fclgj fm fwdmslqn
        fpwcnguieh fdw fgixsr yco ycqlinro ylduwpsnh yrx yiq hysucxdqm hdmwpe hgecdfj en emjocsild epgdc
        ermjdhsx lwnepmcg lgchqdin jxhwe rsogxd rseoyl rqw rfimdy rhfl do dcnql dmqpchuyf dwuch dgsloqe
        gcxr ghepqyd ghlyopuncw ghu grewyluhfs us uo ucf ujxqh udr icmqsdj iw ifl iygsex ihncrl ienqm irmcunfgx
        igxweo ignpeyf"""
        sorted_ = sorted_.replace('\n','')
        sorted_ = sorted_.replace('\t','')
        sorted_ = sorted_.replace('       ','')
        
        # run algorithm
        self.solution.set_text_str(test1)
        self.solution.run()
        
        cond = self.solution.prepositions == 3
        cond &= self.solution.verbs == 36
        cond &= self.solution.subjuntives == 25
        cond &= self.solution.pretty_numbers == 22
        cond &= ' '.join(self.solution.ordered) == sorted_
        assert cond == True

        

    def test_two(self):
        
        test2 = """dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh efwh
        uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs qncuyiel hwuiqlne
        umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos djpsogiy xyp myngercj yeujqcoih
        sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc
        xhrjyocde mnefpj rcyihwxq oihjwrup gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs
        cghuwpfxly ifwpnx wqdgrl xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc
        jqwpdo eo hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm jnufdshiqe
        liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc"""

        sorted_ = """sqemywlg snp swfruc sdhfnoxg sgljco silruxh xocpjedsfm xchm xcdupho xy xyp
        xhrjyocde xrhm xuedl oxmegsdi oegli ous oihjwrup csxpy cnfimrgows cnyosu cwoen ceqrugs cjlxoiquef
        cghuwpfxly qncuyiel qgro nqpge nqhodjsm ndis mnefpj myngercj meod wqdgrl wmi wixmhcuynj poy
        pmrs fxdn fwqrijemcd fyejhi fhnwomgyuq fjnomcledi frqog yp yeujqcoih yj hc hcgeox hqsgcy hnxyfd
        hmypjfu hwuiqlne hyfgqj heixgmcy hlwgimn exmdnos eo eopq eofxlrd eqxghfry eqclrnguo efwh
        ehyldsnmf euhxmosc eujh lqeshijndg lf lhimoynsr lruneodc liyrexhmu jqwpdo jnufdshiqe jwroheqm
        jwispgefdo rxoew rcyihwxq rnc rwjxecpmfl rfs rylnsph dniefl djpsogiy drg dufqwh gquscxhw gm gywlc
        gimqxwuyr uxfrpsnqd ucrfdsoeq uqpwmni umynehjsci umyldn uwflpqc url ugnmqfypsd ifwpnx iecusqjp
        ijucmxw"""
        sorted_ = sorted_.replace('\n','')
        sorted_ = sorted_.replace('\t','')
        sorted_ = sorted_.replace('       ','')
        
        # run algorithm
        self.solution.set_text_str(test2)
        self.solution.run()
        
        cond = self.solution.prepositions == 3
        cond &= self.solution.verbs == 46
        cond &= self.solution.subjuntives == 26
        cond &= self.solution.pretty_numbers == 21
        cond &= ' '.join(self.solution.ordered) == sorted_
        assert cond == True

    def test_three(self):

        test3 = """xerni hej meofh nowmfjhgur qsixdwp rwgfe xigldpnw nl jgnmqpesy dwh wiergnlpfj unei lgxidjs lyq pde ju
        merwcxu xqgjeo iqfwyh rq xgdmopqhy qfderyjc lwrjsoynp miwlehxjcr xmry oncfipjg sgd dycjrflsn woyi lx
        ousryfgcqp sxrhen gucfdpx edyn xngjhweodm xfujp lqyuch mr cjywmpuqns dfcugqws piuerlxhm cjh rgeoj
        xucq impuhyec uhswgnpfj rl ngmwdeh ionxw uhisd dprhwqun yf gnepqwymuj wiylruxcqg fmnpo
        wxcjemsuf wsijx nriy usqioe coeslhu ce chdo ydqsgjlhfn rihluydngf fq yrmejs xqcjwsdi prydlnc hxcl
        ngrxcumijs sunrdwm urflyq jmcsorwglx gelnif esc ymfswnqij ifdn rfegusyj fw uinefd wsuxc lsjyndqgx
        leginjo jiqwscle gdiusxecqj oufqgmjh dunw eyscgxulwn xfjdiy yodi rfhdclgo sngrmj wc rfd hfnjc yijf
        yjurqsomp ogmycfqnrh gmuxsijo dqmyeugjlo"""

        sorted_ = """sxrhen sngrmj sgd sunrdwm xqcjwsdi xqgjeo xngjhweodm xmry xfjdiy xfujp xerni
        xgdmopqhy xucq xigldpnw oncfipjg ogmycfqnrh ousryfgcqp oufqgmjh coeslhu chdo ce cjywmpuqns cjh
        qsixdwp qfderyjc nowmfjhgur nl nriy ngmwdeh ngrxcumijs meofh merwcxu mr miwlehxjcr wsuxc wsijx
        wxcjemsuf woyi wc wiylruxcqg wiergnlpfj prydlnc pde piuerlxhm fq fmnpo fw yodi ymfswnqij yf yjurqsomp
        yrmejs ydqsgjlhfn yijf hxcl hfnjc hej esc eyscgxulwn edyn lsjyndqgx lx lqyuch lwrjsoynp lyq leginjo lgxidjs
        jmcsorwglx jgnmqpesy ju jiqwscle rq rwgfe rfhdclgo rfegusyj rfd rl rgeoj rihluydngf dqmyeugjlo dwh
        dprhwqun dfcugqws dycjrflsn dunw gnepqwymuj gmuxsijo gelnif gdiusxecqj gucfdpx usqioe unei
        uhswgnpfj uhisd urflyq uinefd ionxw iqfwyh impuhyec ifdn"""
        sorted_ = sorted_.replace('\n','')
        sorted_ = sorted_.replace('\t','')
        sorted_ = sorted_.replace('       ','')
        
        # run algorithm
        self.solution.set_text_str(test3)
        self.solution.run()
        
        cond = self.solution.prepositions == 2
        cond &= self.solution.verbs == 37
        cond &= self.solution.subjuntives == 22
        cond &= self.solution.pretty_numbers == 27
        cond &= ' '.join(self.solution.ordered) == sorted_
        assert cond == True

    def test_four(self):

        test4 = """fdmrsl lfro lxng cn jywenuqr mdgr pirfd puisec muf oupmifrn dr xyigmqwp cnomj unowmxiecd
        odprsxwqge dyuhwxc ihpslwgoqm gwucos jcoer oelyg hmsp qenfdjrhcu csj fd ow jsuh oghqepxjlc jui
        yupjenqmf jndfyqm qsdmjlf yghuecdj fhsogp hiwn neiwlogrsy ysw lcyehfi qd us oshnxrfpd ohx njdy yqwxn
        osxjdqf qd somhefcix ofhledm ulrosdm gh dowueprmc pxryc smoxlwfnr pnciyrl us xjomhfe qlw jcfye
        fcqlpoiu xeohlq mrsylhxwqf mxdplruge yumrfio cnyxdm xchidjpe fn cjupdxnefm ig icwgux qcfopnmey
        ryshjxdc yricqxhfeo opdlfnhu rcpdlo oclmyr hpjfnlqy lnsdioe ojirm nfcmxjwgl wqphu eunyd eopi feru
        hgwcms fu dmgxjholu ls owupc iw nxgupwhl udjnylie uewdymsl sypmcelu sup qdlhjmeno nrxu csiex
        fuqrlid hmie fxgs nsjopuw"""

        sorted_ = """somhefcix smoxlwfnr sypmcelu sup xchidjpe xyigmqwp xeohlq xjomhfe osxjdqf
        oshnxrfpd oclmyr ow owupc opdlfnhu ofhledm ohx oelyg ojirm odprsxwqge oghqepxjlc oupmifrn csj csiex
        cn cnomj cnyxdm cjupdxnefm qsdmjlf qcfopnmey qenfdjrhcu qlw qd qdlhjmeno nsjopuw nxgupwhl
        nfcmxjwgl neiwlogrsy njdy nrxu mxdplruge mrsylhxwqf mdgr muf wqphu pxryc pnciyrl puisec pirfd fxgs
        fcqlpoiu fn fhsogp feru fd fdmrsl fu fuqrlid ysw yqwxn yricqxhfeo yghuecdj yumrfio yupjenqmf hmsp hmie
        hpjfnlqy hgwcms hiwn eopi eunyd ls lxng lcyehfi lnsdioe lfro jsuh jcoer jcfye jndfyqm jywenuqr jui rcpdlo
        ryshjxdc dowueprmc dmgxjholu dyuhwxc dr gwucos gh us unowmxiecd uewdymsl ulrosdm udjnylie
        icwgux iw ihpslwgoqm ig"""
        sorted_ = sorted_.replace('\n','')
        sorted_ = sorted_.replace('\t','')
        sorted_ = sorted_.replace('       ','')
        
        # run algorithm
        self.solution.set_text_str(test4)
        self.solution.run()
        
        cond = self.solution.prepositions == 3
        cond &= self.solution.verbs == 31
        cond &= self.solution.subjuntives == 19
        cond &= self.solution.pretty_numbers == 27
        cond &= ' '.join(self.solution.ordered) == sorted_
        assert cond == True

    def test_five(self):

        filename = 'test.txt'

        sorted_ = """sxwc syjqfr srhm sinprhlwdm xwqmucp xwule ocmhp oylfmierg ojgelhisc orl odi oux
        cndlxuqhfg cpgyx ch cjxdl cgr ciex qpngufxjli qhiwfyudsp qehcmrjpwu qljs qrj qugre nsdohjim ncjysiwdh
        nqc nqeduhc ndepfswml ms mqgwclf mwrpcg mfginrqulc mexfjsi mjrliogucs mgnoqdjh muoplcrfi
        wxmyhipou wpxgyh wydjx wisly pxiomfqwrd pqf pmldxecqf pysfieucx phlyf phdgqir peqfw fsxcerumow
        fqexsi fwerpnxogs yqmgihus ywcr ypwocmxni yedhpws ylnxequr yjgq yrshie yinjs hsfywx hwsqc hwmjp
        hpngdocxw hygu hjwsqel hdroml hgcmqix exsij eorq ec eq emnd epqdonschm ey edmpwfnsuh lx ljsf jnqul
        jrcdiye jimlxfsygc rxsfecil rnpjw rjoh rijpsfgm dje dimxwofheq goi gn gnl uspxjgdlei umwrc umrocw up
        ufidryq isxl icy ipoufr iyuq irplxyofsm iupdjfnhm"""
        sorted_ = sorted_.replace('\n','')
        sorted_ = sorted_.replace('\t','')
        sorted_ = sorted_.replace('       ','')
        
        # run algorithm
        self.solution.set_text_file(filename)
        self.solution.run()
        
        cond = self.solution.prepositions == 1
        cond &= self.solution.verbs == 32
        cond &= self.solution.subjuntives == 19
        cond &= self.solution.pretty_numbers == 26
        cond &= ' '.join(self.solution.ordered) == sorted_
        assert cond == True
        
    
    def teardown_method(self, method):
        del self.solution






