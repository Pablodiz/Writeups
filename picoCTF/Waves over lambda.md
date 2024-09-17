Fecha: 18/09/2024

El reto nos pide que nos conectemos por netcat a una dirección y puerto, y nos devuelve este texto:
```
-------------------------------------------------------------------------------
jtpzscvh edsd kh rtbs xicz - xsdmbdpjr_kh_j_tnds_icuoyc_tzxucbpscx
-------------------------------------------------------------------------------
odvqddp bh vedsd qch, ch k ecnd cisdcyr hcky htudqedsd, ved otpy tx ved hdc. odhkydh etiykpz tbs edcsvh vtzdveds vestbze itpz wdsktyh tx hdwcscvktp, kv ecy ved dxxdjv tx ucfkpz bh vtidscpv tx dcje tveds'h rcsphcpy dndp jtpnkjvktph. ved icqrdsved odhv tx tiy xdiitqhecy, odjcbhd tx ekh ucpr rdcsh cpy ucpr nksvbdh, ved tpir jbhektp tp ydjf, cpy qch irkpz tp ved tpir sbz. ved cjjtbpvcpv ecy ostbzev tbv cisdcyr c ota tx ytukptdh, cpy qch vtrkpz csjekvdjvbsciir qkve ved otpdh. ucsitq hcv jsthh-idzzdy skzev cxv, idcpkpz czckphv ved ukggdp-uchv. ed ecy hbpfdp jeddfh, c rdiitq jtuwidaktp, c hvsckzev ocjf, cp chjdvkj chwdjv, cpy, qkve ekh csuh ystwwdy, ved wciuh tx ecpyh tbvqcsyh, sdhduoidy cp kyti. ved yksdjvts, hcvkhxkdy ved cpjets ecy ztty etiy, ucyd ekh qcr cxv cpy hcv ytqp cutpzhv bh. qd dajecpzdy c xdq qtsyh icgkir. cxvdsqcsyh vedsd qch hkidpjd tp otcsy ved rcjev. xts htud sdchtp ts tveds qd yky ptv odzkp vecv zcud tx ytukptdh. qd xdiv udykvcvknd, cpy xkv xts ptvekpz obv wicjky hvcskpz. ved ycr qch dpykpz kp c hdsdpkvr tx hvkii cpy dambkhkvd oskiikcpjd. ved qcvds hetpd wcjkxkjciir; ved hfr, qkvetbv c hwdjf, qch c odpkzp kuudphkvr tx bphvckpdy ikzev; ved ndsr ukhv tp ved dhhda ucshe qch ikfd c zcbgr cpy scykcpv xcoskj, ebpz xstu ved qttydy skhdh kpicpy, cpy yscwkpz ved itq hetsdh kp ykcwecptbh xtiyh. tpir ved zittu vt ved qdhv, osttykpz tnds ved bwwds sdcjedh, odjcud utsd htuosd dndsr ukpbvd, ch kx cpzdsdy or ved cwwstcje tx ved hbp.

```

Además, en el enunciado del reto dice que han hecho "muchas sustituciones". Lo primero que pruebo es si es cesar, sin éxito. Luego, pruebo con [mono-alphabetic substitution](https://www.dcode.fr/monoalphabetic-substitution), consiguiendo descifrarlo: 

```
------------------------------------------------------------------------------- CONGRATS HERE IS YOUR FLAG - FREQUENCY_IS_C_OVER_LAMBDA_OGFMAUNRAF 
------------------------------------------------------------------------------- 
BETWEEN US THERE WAS, AS I HAVE ALREADY SAID SOMEWHERE, THE BOND OF THE SEA. BESIDES HOLDING OUR HEARTS TOGETHER THROUGH LONG PERIODS OF SEPARATION, IT HAD THE EFFECT OF MAKING US TOLERANT OF EACH OTHER'S YARNSAND EVEN CONVICTIONS. THE LAWYERTHE BEST OF OLD FELLOWSHAD, BECAUSE OF HIS MANY YEARS AND MANY VIRTUES, THE ONLY CUSHION ON DECK, AND WAS LYING ON THE ONLY RUG. THE ACCOUNTANT HAD BROUGHT OUT ALREADY A BOJ OF DOMINOES, AND WAS TOYING ARCHITECTURALLY WITH THE BONES. MARLOW SAT CROSS-LEGGED RIGHT AFT, LEANING AGAINST THE MIXXEN-MAST. HE HAD SUNKEN CHEEKS, A YELLOW COMPLEJION, A STRAIGHT BACK, AN ASCETIC ASPECT, AND, WITH HIS ARMS DROPPED, THE PALMS OF HANDS OUTWARDS, RESEMBLED AN IDOL. THE DIRECTOR, SATISFIED THE ANCHOR HAD GOOD HOLD, MADE HIS WAY AFT AND SAT DOWN AMONGST US. WE EJCHANGED A FEW WORDS LAXILY. AFTERWARDS THERE WAS SILENCE ON BOARD THE YACHT. FOR SOME REASON OR OTHER WE DID NOT BEGIN THAT GAME OF DOMINOES. WE FELT MEDITATIVE, AND FIT FOR NOTHING BUT PLACID STARING. THE DAY WAS ENDING IN A SERENITY OF STILL AND EJQUISITE BRILLIANCE. THE WATER SHONE PACIFICALLY; THE SKY, WITHOUT A SPECK, WAS A BENIGN IMMENSITY OF UNSTAINED LIGHT; THE VERY MIST ON THE ESSEJ MARSH WAS LIKE A GAUXY AND RADIANT FABRIC, HUNG FROM THE WOODED RISES INLAND, AND DRAPING THE LOW SHORES IN DIAPHANOUS FOLDS. ONLY THE GLOOM TO THE WEST, BROODING OVER THE UPPER REACHES, BECAME MORE SOMBRE EVERY MINUTE, AS IF ANGERED BY THE APPROACH OF THE SUN.
```

Como el texto original está en minúsculas, hay que cambiar la flag un poco:
`picoCTF{frequency_is_c_over_lambda_ogfmaunraf}`

El reto no acepta el flag. 