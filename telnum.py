#!/usr/bin/env python3
# encoding: utf-8 (as per PEP 263)

import sys

try:
    import phonenumbers
    from phonenumbers import geocoder, PhoneNumberType
except:
    raise Exception('Could not find module "phonenumbers".\nTry `pip3 install phonenumbers`.\n')

def number_to_text(num):
    try:
        if not num.startswith('+'):
            num = '+' + num
        if not num.endswith('\n'):  # last line
            num = num + '\n'

        x = phonenumbers.parse(num)

        def number_type_desc(num_type):
            if num_type == PhoneNumberType.PREMIUM_RATE:
                return 'premium-rate'
            elif num_type == PhoneNumberType.TOLL_FREE:
                return 'toll-free'
            elif num_type == PhoneNumberType.MOBILE:
                return 'mobile'
            elif num_type == PhoneNumberType.FIXED_LINE:
                return 'fixed-line'
            elif num_type == PhoneNumberType.FIXED_LINE_OR_MOBILE:
                return 'fixed-line or mobile'
            elif num_type == PhoneNumberType.SHARED_COST:
                return 'shared cost'
            elif num_type == PhoneNumberType.VOIP:
                return 'VoIP'
            elif num_type == PhoneNumberType.PERSONAL_NUMBER:
                return 'personal number'
            elif num_type == PhoneNumberType.PAGER:
                return 'pager'
            elif num_type == PhoneNumberType.UAN:
                return 'company "universal access number"'
            elif num_type == PhoneNumberType.VOICEMAIL:
                return 'voicemail'
            else:
                return 'unknown type'

        number = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        numtype = number_type_desc(phonenumbers.number_type(x))
        country = geocoder.country_name_for_number(x, "en")
        desc = geocoder.description_for_number(x, "en")

        if not desc or desc == country:
            return '%s\n%s - %s' % (number, country, numtype)
        else:
            return '%s\n%s, %s - %s' % (number, desc, country, numtype)

    except:
        return '%sinvalid' % (num)

def main():
    if len(sys.argv) > 1:
        nums = sys.argv[1:]
    else:
        nums = sys.stdin.readlines()
        nums = map(strip, nums)

    for num in nums:
        print(number_to_text(num))

if __name__ == '__main__':
    main()
