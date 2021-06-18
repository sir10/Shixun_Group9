import glob
import json
import re

youji_detail_paths = glob.glob('.\\youji_detail\\*.json')
# count = 0
for youji_detail_path in youji_detail_paths:
    with open(youji_detail_path, 'r', encoding='utf-8') as f:
        youji_json = json.load(f)
    youji_json_format = []
    i = 0
    city_name = youji_detail_path.split('\\')[-1].split('_')[0]
    for youji_item in youji_json:

        # 去空
        if youji_item['title'] == '':
            continue

        # 主体内容去空白
        content = youji_item['content']
        # content.replace('\ue653', '')
        # re.compile('\n|\t|\\s|\\ue653')
        # content = ''.join(content.split())
        youji_item['content'] = re.sub('\ue653|\s+', '', content)
        with open('./youji/'+city_name+'/{}.txt'.format(str(i)), 'w', encoding='utf-8') as f_content:
            f_content.write(content)
        i += 1

        # 出发时间
        start_date = youji_item['start_date']
        if start_date != '':
            # start_date_info = re.compile('出发时间')
            # start_date = re.sub(start_date_info, '', start_date)
            start_date = re.findall('\d+', start_date)[0]
        else:
            start_date = '0'
        youji_item['start_date'] = start_date

        # 行程天数
        out_day = youji_item['out_day']
        if out_day != '':
            # out_day_info = re.compile('行程天数')
            # out_day = re.sub(out_day_info, '', out_day)
            out_day = re.findall('\d+', out_day)[0]
        else:
            out_day = '0'
        youji_item['out_day'] = out_day

        # 和谁出行
        whom_with = youji_item['whom_with']
        if whom_with != '':
            whom_with_info = re.compile('和谁出行')
            whom_with = re.sub(whom_with_info, '', whom_with)
        youji_item['whom_with'] = whom_with

        # 人均花费
        aver_cost = youji_item['aver_cost']
        if aver_cost != '':
            aver_cost_info = re.compile('人均花费')
            aver_cost = re.sub(aver_cost_info, '', aver_cost)
        else:
            aver_cost = '0'
        youji_item['aver_cost'] = aver_cost

        # URL
        url = youji_item['url']
        url = re.sub(re.compile('\n'), '', url)
        youji_item['url'] = url

        youji_json_format.append(youji_item)

    # print(len(youji_json_format))
    # count += len(youji_json_format)
    with open(youji_detail_path, 'w', encoding='utf-8') as f1:
        json.dump(youji_json_format, f1, ensure_ascii=False, indent=4)
print('Finish!!!!')