import requests

url = "https://shop.lululemon.com/api/p/womens-leggings/Align-Crop-23-Diamond-Dye/_/prod10080054"

payload = {}
headers = {
    'Cookie': 'Country=US; UsrLocale=en_US; _abck=DAECF3BCBC0AF1AB968EF63341FBC717~-1~YAAQxnTZFxcQx3V4AQAAA5lWrAUaYGQHvNxEruhNDjvTn7JcKq6G0Og3qABx0QrG+FxKppJbM2GzqQsKuxR6lk6gPub6Jh3q0YSn18eIl19NLl1gaNYLyMESNdxBtkDJlB/mqC3m7KMiShe5Jg45GGAEI5OHoU3TZaN3tmZvUxv9lYu8h/tc2ZiDEjZSCO0IJOeyITOL+QMA/7nmSq7WQ/TUfQeM5y1eagWOsbWwSmyIvs3iRwSmRxnSNg1cnHd0zMyqRz73X8o2SLPhD+5AlPxlFjiG9buMRL9FbZbPQvkefJTDEw25xzbK6BD9uFuTXZ9E6DXn71+tlBkJTm4q0j5/zoR3GVivs70+FEvdF27NF7hCRnobE2PXwzMlEi/pQ/kgsu5tFGn2ZQ==~-1~-1~-1; bm_sz=E8F1E6E7183CDF06D4A45754B5A2C42C~YAAQxnTZFxYQx3V4AQAAA5lWrAt3RbY+PR9CgVwTgbLfItiTJhslk1Cgd8RRU1liAkQiFYPwUO9YOU+AMU3lPB5EmAt9PM00yZNBgW2TMr2RaJWC/o4h2t5u/pGLWjCOayvEGGqSvUT4fx3nSHXasXi2WMuJNXZDSPmu7mMcA/Mud856s9B8jfnSMAl1Z7gG8MZ9; cartCount=0; digitalData.page.a1Token=$2a$10$mPfoQjvIP1yLqNTUT44K5utr.Tdd7G/vuKP3P2clWHXNJDVQYoQQG; isLoggedin=false; ltmo=2; sl=US; us_ord="ZmDlaGVDd+q8LMPf+UznYg=="; us_ord_stores="ZmDlaGVDd+q8LMPf+UznYg==<|>XzGjq9zxQ8E="; userPrefLanguage=en_US; JSESSIONID=M76sVpVHX10-Mm6um997WQ6YxLM_9i8Bot1zqFQiAwOjTEH267jq!-704106143; WLS_ROUTE=.156; lll-ecom-correlation-id=D2751C8F-9050-33D1-950F-3C758A0EABBC'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
