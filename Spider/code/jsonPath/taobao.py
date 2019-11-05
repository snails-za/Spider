import urllib.request
import json
import jsonpath


def main():
    url = r'https://rate.taobao.com/feedRateList.htm?auctionNumId=565524655319&userNumId=813854980&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hvTQv8vWyvUvCkvvvvvjiPRszw1j3PPFLO0jivPmPUgjYbPLFOzjn2P2q9ljE8dphvmpmC8ms2vvm22UwCvvpv9hCvmphvLvCn9IUafXeKHsyDZtcEKfUZDVQEfwkK5d8rwoAgufJ6n1Bkp8oQ%2Bu0Xd56Ofwp4du0AVADlaBoAdBQanbmxdX9Xd56OfwAKHd8rwZ7ivpvUvvCCbWNCUWKEvpvV9pCmpYFyKphv8PMMpbFMMQCGvvCHhQvvvZwvvhZLvvmCvvvvBBWvvvH%2BvvCHUQvvvcpCvpvVvUCvpvvv2QhvCvvvMMGtvpvhvvCvp8wCvvpvvhHh&_ksTS=1571713738497_1269&callback=jsonp_tbcrate_reviews_list&sm'
    headers = {
        'Connection': 'keep - alive',
        'Accept': '* / *',

        # 'Host': 'rate.taobao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        # 'Cookie': 'miid=440409881939950827; t=3e603efd2b5b81b7fc0e8ae7fff3d1e7; cna=UbpSFVMSAlsCAXUktQ5Mdn5w; isg=BLi41FEUEbVcv335WVHC_L8VimZABbGowC2RLPIon_OXDVn3mjAJOpJjwdUYRtSD; l=dBg_afbnqF4u6CCvBOfZNZ1AJk7T0Id48kPPhe1WMICPOKCekkllWZIep7YwCn6Vns3BR3R0jrkJBA8E7y4ECEGfIqlBs2JZEdLh.; thw=cn; tracknick=byle0000; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; enc=rG5jPvGm0sAGpyHUKBaGVVBr3CYiFoKnoYGYHgC0VBEN5JOLBxSLTL%2Fluz8HBg131ZS2nc1%2FH7EDfpNBGEU0%2BA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; _m_h5_tk=bdb147011b830f57ce6c1f0f6aba56c2_1571665896536; _m_h5_tk_enc=65c8ff4970596125d98956f1e0ef4a2a; mt=ci%3D-1_1; cookie2=132ffbb2da9eb8f16980552fddd0fef6; v=0; _tb_token_=31363eb8eb33b; x5sec=7b22726174656d616e616765723b32223a226361326439333466326237336335663838636437353063306461363066366532434a6d2f74753046454c4c6f396361763739334c62673d3d227d'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request).read().decode()
    # response = json.loads(response)
    print(response)
    # comments = response["comments"]
    # print(comments)


if __name__ == '__main__':
    main()
