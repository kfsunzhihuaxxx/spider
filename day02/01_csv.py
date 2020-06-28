import csv



with open('spider.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['步惊云','绝世好剑'])

# newline参数仅仅局限于windows环境下
with open('spider.csv','a',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([('聂风','血饮狂刀'),('星矢','天马流星拳')])

