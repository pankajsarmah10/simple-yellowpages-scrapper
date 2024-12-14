import os
import constants
import utils

data = []
search_text = os.getenv("search_text")
counter = 0
for i in range(1, utils.get_total_pages(search_text) + 1):
    tree = utils.get_parsed_response(search_text, i)
    boxes = tree.xpath(constants.SEARCH_RESULT_ROWS)
    for box in boxes:
        counter += 1
        name = box.xpath(constants.LINK_NAME)[0]
        verified = "YES" if box.xpath(constants.IMG_VERIFIED) else 'NO'
        location = location_text[0] if (location_text := box.xpath(constants.LABEL_LOCATION)) else 'NA'
        city = city_text[0] if (city_text := box.xpath(constants.LABEL_CITY)) else 'NA'
        po_box = pobox_text[0] if (pobox_text := box.xpath(constants.LABEL_POBOX)) else 'NA'
        phone = primary_phone_text[0] if (primary_phone_text := box.xpath(constants.LABEL_PHONE)) else 'NA'
        mobile_phone_1 = mobile_phone_1_text[0] if (mobile_phone_1_text := box.xpath(constants.LABEL_MOBILE_1)) else 'NA'
        mobile_phone_2 = mobile_phone_2_text[0] if (mobile_phone_2_text := box.xpath(constants.LABEL_MOBILE_2)) else 'NA'
        website = website_text[0] if (website_text := box.xpath(constants.BUTTON_WEBSITE)) else 'NA'

        data.append({
            'Sl.No.': counter,
            'Name': name,
            'Verified': verified,
            'Location': location,
            'City': city,
            'P.O Box': po_box,
            'Phone': phone,
            'Mobile Phone 1': mobile_phone_1,
            'Mobile Phone 2': mobile_phone_2,
            'Website': website
        })

utils.extract_to_excel(data)