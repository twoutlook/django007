# print ("#========== http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python")

def make_src():
    # 一次性讀入規格
    f1=open('ITEM009.txt')
    lines=f1.readlines()
    f1.close()
    
    # 寫入 cola,colb,colc,colf 
    # cola = colb = colc = colf = [] #在這裡是不行的!
    colA = [] 
    colB = [] 
    colC = [] 
    colG = [] 
   
    outTh = '<tr>'   
    for th in range(1,21):
        outTh += '<th>' + str(th) + '</th>'   
    outTh += '</tr>'   
    
    i = 0
    for line in lines:
        i += 1
        seq = "{0:02d}".format(i)
        sects = line.split("|") 
        colA.append(sects[0])
        colB.append(sects[1])
        colC.append(sects[2])
        colG.append(sects[3].rstrip())
    # 
    out0 = '### 顯示需求基模版\n'
    out1 = '### source code for models\n'
    out2 = '### source code for template\n'
    v=0
    for  v1,v2,v3,v4 in zip(colA,colB,colC,colG):
        v += 1
        #
        out0 += "    <tr><th>{0:d}</th><th>{1}</th><th>{2}</th><td>{3}</td><td></td><td></td><td></td><td colspan='2'>{4}</td></tr>\n".format(v,v1,v2, v3,v4)
    
    
    # rem = colf
    # for  v1,v2,v3,v4 in zip(cola,colb,colc, rem):
        # print ("    <tr><th>{0:s}</th><th>{1:s}</th><td>{2:s}</td><td></td><td></td><td></td><td colspan='2'>{3:s}</td></tr>".format(v1,v2, v3,v4))
        # a='    data{0:02d}a = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 零件")'.format(v, v1, v2)
        # b='    data{0:02d}b = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度一")'.format(v, v1, v2)
        # c='    data{0:02d}c = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度二")'.format(v, v1, v2)
        # d='    data{0:02d}d = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度三")'.format(v, v1, v2)
        # e='    data{0:02d}e_00 = models.NullBooleanField(verbose_name="{1:s} {2:s} 備註說明  正常")'.format(v,v1, v2)
    
        # data01e_00 = models.NullBooleanField(verbose_name="格林柱-備註說明-正常")
        # data01e_01 = models.NullBooleanField(verbose_name="格林柱-備註說明-磨損")
        
        if (len(v3)>0):
            out1 += '    row{0:02d}c__ = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 零件")\n'.format(v, v1, v2)
            parts = v3.split(".")
            i=0
            for part in parts:
                i += 1
                out1 +='    row{0:02d}c{1:02d} = models.NullBooleanField(verbose_name="{2:s} {3:s} 零件 => {4:s}")\n'.format(v,i,v1, v2, part)
            out1 += '    row{0:02d}d__ = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度一")\n'.format(v, v1, v2)
            out1 += '    row{0:02d}e__ = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度二")\n'.format(v, v1, v2)
            out1 += '    row{0:02d}f__ = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度三")\n'.format(v, v1, v2)
            out1 += '    row{0:02d}g__ = models.NullBooleanField(verbose_name="{1:s} {2:s} 備註說明  正常")\n'.format(v,v1, v2)
            
        if (len(v4)>0):
            rems = v4.split(".")
            i=0
            for rem in rems:
                i += 1
            out1 += '    row{0:02d}g{1:02d} = models.NullBooleanField(verbose_name="{2:s} {3:s} 備註說明 => {4:s}")\n'.format(v, i, v1,v2,rem)
    
    
    
   
    # by Mark, 2016-08-27
    output=[]
    output.append(outTh)
    output.append(out0)
    output.append(out1)
    # output.append(out2)
    
    return output
    
#     v=0
# for  v1,v2,v3,v4 in zip(cola,colb,colc, rem):
#     # print ("    <tr><th>{0:s}</th><th>{1:s}</th><td>{2:s}</td><td></td><td></td><td></td><td colspan='2'>{3:s}</td></tr>".format(v1,v2, v3,v4))
#     v += 1
#     a='    data{0:02d}a = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 零件")'.format(v, v1, v2)
#     b='    data{0:02d}b = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度一")'.format(v, v1, v2)
#     c='    data{0:02d}c = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度二")'.format(v, v1, v2)
#     d='    data{0:02d}d = models.CharField(default=".",max_length=99,verbose_name="{1:s} {2:s} 進度三")'.format(v, v1, v2)
#     e='    data{0:02d}e_00 = models.NullBooleanField(verbose_name="{1:s} {2:s} 備註說明  正常")'.format(v,v1, v2)

#     print("###")
#     # print(a)
    
#     # data01e_00 = models.NullBooleanField(verbose_name="格林柱-備註說明-正常")
#     # data01e_01 = models.NullBooleanField(verbose_name="格林柱-備註說明-磨損")
    
#     if (len(v3)>0):
#         parts = v3.split("|")
#         i=1
#         for part in parts:
#             # print (part)    
#             axx='    data{0:02d}a_{1:02d} = models.NullBooleanField(verbose_name="{2:s} {3:s} 零件  {4:s}")'.format(v,i,v1, v2, part)
#             print (axx)    
#             i += 1
            
#     print(b)
    
#     print(c)
#     print(d)
#     print(e)
    
    
#     if (len(v4)>0):
#         rems = v4.split("|")
#         i=1
#         for rem in rems:
#             # print (rem)    
#             exx='    data{0:02d}e_{1:02d} = models.NullBooleanField(verbose_name="{2:s} {3:s} 備註說明  {4:s}")'.format(v, i, v1,v2,rem)
#             print (exx)    
#             i += 1
 
    
# read1()



with open('ITEM009-SRC.txt','w') as out:
    for data in make_src():
        out.write('\n\n\n')
        out.write(data)


# read2()
# read3()
# read4()
