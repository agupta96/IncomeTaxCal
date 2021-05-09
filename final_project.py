list1= ["FICA", "retirement savings" , "state income" , "Federal income"]

print ("Welcome, This income tax calculator will dertermine:", list1, "from your income")


state = input("Enter state: ")
status = input("Enter your filing status: ")
income = float(input("Enter your income: $"))


if state == "Alabama":
    def al(al_income):
        if status == "single":
            if al_income <= 500:
                return al_income * 0.02
            elif al_income <= 3000:
                return 500 * 0.02 + (al_income - 500) * 0.04
            else:
                return 500 * 0.02 + (3000 - 500) * 0.02 + (al_income - 3000) * 0.05

        elif status == "married filed jointly":
            if al_income <= 1000:
                return al_income * 0.02
            elif al_income <= 6000:
                return 1000 * 0.02 + (al_income - 1000) * 0.04
            else:
                return 1000 * 0.02 + (6000 - 1000) * 0.04 + (al_income - 6000) * 0.05

        elif status == "married filed separately":
            if al_income <= 500:
                return al_income * 0.02
            elif al_income <= 3000:
                return 500 * 0.02 + (al_income - 500) * 0.04
            else:
                return 500 * 0.02 + (3000 - 500) * 0.04 + (al_income - 3000) * 0.05

        elif status == "head of household":
            if al_income <= 500:
                return al_income * 0.02
            elif al_income <= 3000:
                return 500 * 0.02 + (al_income - 500) * 0.04
            else:
                return 500 * 0.02 + (3000 - 500) * 0.02 + (al_income - 3000) * 0.05

    def print_info(al_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        al_loss = al(al_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - al_loss - fica
        ret_income = income - afterTaxes - al_loss - fica - retirement
        print("Total Alabama state taxes you pay: $", round(al_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Alabama state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Alaska":
    def ak(ak_income):
        return 0

    def print_info(ak_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ak_loss = ak(ak_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ak_loss - fica
        ret_income = income - afterTaxes - ak_loss - fica - retirement
        print("Total Alaska state taxes you pay: $", round(ak_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Alaska state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))




elif state == "Arizona":
    def az(az_income):
        if status == "single":
            if az_income <= 26500:
                return az_income * 0.0259
            elif az_income <= 53000:
                return 26500 * 0.0259 + (az_income - 26500) * 0.0334
            elif az_income <= 159000:
                return 26500 * 0.0259 + (53000 - 26500) * 0.0334 + (az_income - 53000) * 0.0417
            else:
                return 26500 * 0.0259 + (53000 - 26500) * 0.0334 + (159000 - 53000) * 0.0417 + \
                       (az_income - 3750) * 0.045

        elif status == "married filed jointly":
            if az_income <= 53000:
                return az_income * 0.0259
            elif az_income <= 106000:
                return 53000 * 0.0259 + (az_income - 53000) * 0.0334
            elif az_income <= 318000:
                return 53000 * 0.0259 + (106000 - 53000) * 0.0334 + (az_income - 106000) * 0.0417
            else:
                return 53000 * 0.0259 + (106000 - 53000) * 0.0334 +  (318000 - 106000) * 0.0417 + \
                       (az_income - 318000) * 0.0450

        elif status == "married filed separately":
            if az_income <= 26500:
                return az_income * 0.0259
            elif az_income <= 53000:
                return 26500 * 0.0259 + (az_income - 26500) * 0.0334
            elif az_income <= 159000:
                return 26500 * 0.0259 + (53000 - 26500) * 0.0334 + (az_income - 53000) * 0.0417
            else:
                return 26500 * 0.0259 + (53000 - 26500) * 0.0334 + (159000 - 53000) * 0.0417 + \
                       (az_income - 3750) * 0.045

        elif status == "head of household":
            if az_income <= 53000:
                return az_income * 0.0259
            elif az_income <= 106000:
                return 53000 * 0.0259 + (az_income - 53000) * 0.0334
            elif az_income <= 318000:
                return 53000 * 0.0259 + (106000 - 53000) * 0.0334 + (az_income - 106000) * 0.0417
            else:
                return 53000 * 0.0259 + (106000 - 53000) * 0.0334 + (318000 - 106000) * 0.0417 + \
                       (az_income - 318000) * 0.0450

    def print_info(az_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        az_loss = az(az_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - az_loss - fica
        ret_income = income - afterTaxes - az_loss - fica - retirement
        print("Total Arizona state taxes you pay: $", round(az_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Arizona state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Arkansas":
    def ar(ar_income):
        if ar_income <= 4499:
            return ar_income * 0.00
        elif ar_income <= 8899:
            return 4499 * 0.00 + (ar_income - 4499) * 0.02
        elif ar_income <= 13399:
            return 4499 * 0.00 + (8899 - 4499) * 0.02 + (ar_income - 8899) * 0.03
        elif ar_income <= 22199:
            return 4499 * 0.00 + (8899 - 4499) * 0.02 + (13399 - 8899) * 0.03 + \
                       (ar_income - 13399) * 0.034
        elif ar_income <= 37199:
            return 4499 * 0.00 + (8899 - 4499) * 0.02 + (13399 - 8899) * 0.03 + \
                       (22199 - 13399) * 0.034 + (ar_income - 22199) * 0.05
        elif ar_income <= 79300:
            return 4499 * 0.00 + (8899 - 4499) * 0.02 + (13399 - 8899) * 0.03 + \
                       (22199 - 13399) * 0.034 + (37199 - 22199) * 0.05 +\
                       (ar_income - 37199) * 0.06
        else:
            return 4499 * 0.00 + (8899 - 4499) * 0.02 + (13399 - 8899) * 0.03 + \
                       (22199 - 13399) * 0.034 + (37199 - 22199) * 0.05 +\
                       (79300 - 37199) * 0.06 + (ar_income - 79300) * 0.066

    def print_info(ar_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ar_loss = ar(ar_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ar_loss - fica
        ret_income = income - afterTaxes - ar_loss - fica - retirement
        print("Total Arkansas state taxes you pay: $", round(ar_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Arkansas state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "California":
    def ca(ca_income):
        if status == "single":
            if ca_income <= 8932:
                return ca_income * 0.01
            elif ca_income <= 21175:
                return 8932 * 0.01 + (ca_income - 8932) * 0.02
            elif ca_income <= 33421:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (ca_income - 21175) * 0.04
            elif ca_income <= 46394:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 +(33421 - 21175) * 0.04 + \
                       (ca_income - 33421) * 0.06
            elif ca_income <= 58634:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 +(33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (ca_income - 46394) * 0.08
            elif ca_income <= 299508:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (ca_income - 58634) * 0.093
            elif ca_income <= 359407:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (ca_income - 299508) * 0.103
            elif ca_income <= 599012:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (599012 - 299508) * 0.103 + \
                       (ca_income - 359407) * 0.113

            elif ca_income <= 1000000:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (599012 - 299508) * 0.103 + \
                       (599012 - 359407) * 0.113 + (ca_income - 599012) * 0.123
            else:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (599012 - 299508) * 0.103 + \
                       (599012 - 359407) * 0.113 + (1000000 - 599012) * 0.123 + \
                       (ca_income - 1000000) * 0.133

        elif status == "married filed jointly":
            if ca_income <= 17864:
                return ca_income * 0.01
            elif ca_income <= 42350:
                return 17864 * 0.01 + (ca_income - 17864) * 0.02
            elif ca_income <= 66482:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (ca_income - 42350) * 0.04
            elif ca_income <= 92788:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (ca_income - 66482) * 0.06
            elif ca_income <= 117268:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (92788 - 66482) * 0.06 + (ca_income - 92788) * 0.08
            elif ca_income <= 599016:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (92788 - 66482) * 0.06 + (117268 - 92788) * 0.08 + \
                       (ca_income - 117268) * 0.093
            elif ca_income <= 718268:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (92788 - 66482) * 0.06 + (117268 - 92788) * 0.08 + \
                       (599016 - 117268) * 0.093 + (ca_income - 599016) * 0.103
            elif ca_income <= 1198024:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (92788 - 66482) * 0.06 + (117268 - 92788) * 0.08 + \
                       (599016 - 117268) * 0.093 + (718268 - 599016) * 0.103 + \
                       (ca_income - 718268) * 0.113

            elif ca_income <= 2000000:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (92788 - 66482) * 0.06 + (117268 - 92788) * 0.08 + \
                       (599016 - 117268) * 0.093 + (718268 - 599016) * 0.103 + \
                       (1198024 - 718268) * 0.113 + (ca_income - 1198024) * 0.123
            else:
                return 17864 * 0.01 + (42350 - 17864) * 0.02 + (66482 - 42350) * 0.04 + \
                       (92788 - 66482) * 0.06 + (117268 - 92788) * 0.08 + \
                       (599016 - 117268) * 0.093 + (718268 - 599016) * 0.103 + \
                       (1198024 - 718268) * 0.113 + (2000000 - 1198024) * 0.123 + \
                       (ca_income - 2000000) * 0.133

        elif status == "married filed separately":
            if ca_income <= 8932:
                return ca_income * 0.01
            elif ca_income <= 21175:
                return 8932 * 0.01 + (ca_income - 8932) * 0.02
            elif ca_income <= 33421:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (ca_income - 21175) * 0.04
            elif ca_income <= 46394:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 +(33421 - 21175) * 0.04 + \
                       (ca_income - 33421) * 0.06
            elif ca_income <= 58634:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 +(33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (ca_income - 46394) * 0.08
            elif ca_income <= 299508:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (ca_income - 58634) * 0.093
            elif ca_income <= 359407:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (ca_income - 299508) * 0.103
            elif ca_income <= 599012:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (599012 - 299508) * 0.103 + \
                       (ca_income - 359407) * 0.113

            elif ca_income <= 1000000:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (599012 - 299508) * 0.103 + \
                       (599012 - 359407) * 0.113 + (ca_income - 599012) * 0.123
            else:
                return 8932 * 0.01 + (21175 - 8932) * 0.02 + (33421 - 21175) * 0.04 + \
                       (46394 - 33421) * 0.06 + (58634 - 46394) * 0.08 + \
                       (299508 - 58634) * 0.093 + (599012 - 299508) * 0.103 + \
                       (599012 - 359407) * 0.113 + (1000000 - 599012) * 0.123 + \
                       (ca_income - 1000000) * 0.133

        elif status == "head of household":
            if ca_income <= 17864:
                return ca_income * 0.01
            elif ca_income <= 42353:
                return 17864 * 0.01 + (ca_income - 17864) * 0.02
            elif ca_income <= 54597:
                return 17864 * 0.01 + (42353 - 17864) * 0.02 + (ca_income - 42353) * 0.04
            elif ca_income <= 67569:
                return 17864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (ca_income - 54597) * 0.06
            elif ca_income <= 79812:
                return 17864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (67569 - 54597) * 0.06 + (ca_income - 67569) * 0.08
            elif ca_income <= 407329:
                return 17864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (67569 - 54597) * 0.06 + (79812 - 67569) * 0.08 + \
                       (ca_income - 79812) * 0.093
            elif ca_income <= 488796:
                return 17864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (67569 - 54597) * 0.06 + (79812 - 67569) * 0.08 + \
                       (299508 - 79812) * 0.093 + (ca_income - 407329) * 0.103
            elif ca_income <= 814658:
                return 7864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (67569 - 54597) * 0.06 + (79812 - 67569) * 0.08 + \
                       (299508 - 79812) * 0.093 + (488796 - 407329) * 0.103 + \
                       (ca_income - 488796) * 0.113

            elif ca_income <= 1000000:
                return 7864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (67569 - 54597) * 0.06 + (79812 - 67569) * 0.08 + \
                       (299508 - 79812) * 0.093 + (488796 - 407329) * 0.103 + \
                       (814658 - 488796) * 0.113 + (ca_income - 814658) * 0.123
            else:
                return 7864 * 0.01 + (42353 - 17864) * 0.02 + (54597 - 42353) * 0.04 + \
                       (67569 - 54597) * 0.06 + (79812 - 67569) * 0.08 + \
                       (299508 - 79812) * 0.093 + (488796 - 407329) * 0.103 + \
                       (814658 - 488796) * 0.113 + (1000000 - 814658) * 0.123 + \
                       (ca_income - 1000000) * 0.133

    def print_info(ca_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ca_loss = ca(ca_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ca_loss - fica
        ret_income = income - afterTaxes - ca_loss - fica - retirement
        print("Total California state taxes you pay: $", round(ca_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after California state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Colorado":
    def co(co_income):
        return co_income * 0.0463

    def print_info(co_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        co_loss = co(co_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - co_loss - fica
        ret_income = income - afterTaxes - co_loss - fica - retirement
        print("Total Colorado state taxes you pay: $", round(co_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Colorado state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Connecticut":
    def ct(ct_income):
        if status == "single":
            if ct_income <= 10000:
                return ct_income * 0.03
            elif ct_income <= 50000:
                return 10000 * 0.03 + (ct_income - 10000) * 0.05
            elif ct_income <= 100000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (ct_income - 50000) * 0.055
            elif ct_income <= 200000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (ct_income - 100000) * 0.06
            elif ct_income <= 250000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (200000 - 100000) * 0.06 + (ct_income - 200000) * 0.065
            elif ct_income <= 500000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (200000 - 100000) * 0.06 + (250000 - 200000) * 0.065 +\
                       (ct_income - 250000) * 0.069
            else:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (200000 - 100000) * 0.06 + (250000 - 200000) * 0.065 +\
                       (500000 - 250000) * 0.069 + (ct_income - 500000) * 0.0699

        elif status == "married filed jointly":
            if ct_income <= 20000:
                return ct_income * 0.03
            elif ct_income <= 100000:
                return 20000 * 0.03 + (ct_income - 100000) * 0.05
            elif ct_income <= 200000:
                return 20000 * 0.03 + (100000 - 20000) * 0.05 + (ct_income - 100000) * 0.055
            elif ct_income <= 400000:
                return 20000 * 0.03 + (100000 - 20000) * 0.05 +(2000000 - 100000) * 0.055 + \
                       (ct_income - 200000) * 0.06
            elif ct_income <= 500000:
                return 20000 * 0.03 + (100000 - 20000) * 0.05 +(2000000 - 100000) * 0.055 + \
                       (400000 - 200000) * 0.06 + (ct_income - 400000) * 0.065
            elif ct_income <= 1000000:
                return 20000 * 0.03 + (100000 - 20000) * 0.05 +(2000000 - 100000) * 0.055 + \
                       (400000 - 200000) * 0.06 + (500000 - 400000) * 0.065 +\
                       (ct_income - 50000) * 0.069
            else:
                return 20000 * 0.03 + (100000 - 20000) * 0.05 +(2000000 - 100000) * 0.055 + \
                       (400000 - 200000) * 0.06 + (500000 - 400000) * 0.065 +\
                       (1000000 - 500000) * 0.069 + (ct_income - 1000000) * 0.0699

        elif status == "married filed separately":
            if ct_income <= 10000:
                return ct_income * 0.03
            elif ct_income <= 50000:
                return 10000 * 0.03 + (ct_income - 10000) * 0.05
            elif ct_income <= 100000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (ct_income - 50000) * 0.055
            elif ct_income <= 200000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (ct_income - 100000) * 0.06
            elif ct_income <= 250000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (200000 - 100000) * 0.06 + (ct_income - 200000) * 0.065
            elif ct_income <= 500000:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (200000 - 100000) * 0.06 + (250000 - 200000) * 0.065 +\
                       (ct_income - 250000) * 0.069
            else:
                return 10000 * 0.03 + (50000 - 10000) * 0.05 + (100000 - 2250000) * 0.055 + \
                       (200000 - 100000) * 0.06 + (250000 - 200000) * 0.065 +\
                       (500000 - 250000) * 0.069 + (ct_income - 500000) * 0.0699

        elif status == "head of household":
            if ct_income <= 16000:
                return ct_income * 0.03
            elif ct_income <= 80000:
                return 16000 * 0.03 + (ct_income - 16000) * 0.05
            elif ct_income <= 160000:
                return 16000 * 0.03 + (80000 - 16000) * 0.05 + (ct_income - 80000) * 0.055
            elif ct_income <= 320000:
                return 16000 * 0.03 + (80000 - 16000) * 0.05 + (160000 - 80000) * 0.055 + \
                       (ct_income - 160000) * 0.06
            elif ct_income <= 400000:
                return 16000 * 0.03 + (80000 - 16000) * 0.05 + (160000 - 80000) * 0.055 + \
                       (320000 - 160000) * 0.06 + (ct_income - 320000) * 0.065
            elif ct_income <= 800000:
                return 16000 * 0.03 + (80000 - 16000) * 0.05 + (160000 - 80000) * 0.055 + \
                       (320000 - 160000) * 0.06 + (400000 - 320000) * 0.065 +\
                       (ct_income - 400000) * 0.069
            else:
                return 16000 * 0.03 + (80000 - 16000) * 0.05 + (160000 - 80000) * 0.055 + \
                       (320000 - 160000) * 0.06 + (400000 - 320000) * 0.065 +\
                       (800000 - 40000) * 0.069 + (ct_income - 800000) * 0.0699


    def print_info(ct_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ct_loss = ct(ct_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ct_loss - fica
        ret_income = income - afterTaxes - ct_loss - fica - retirement
        print("Total Connecticut state taxes you pay: $", round(ct_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Connecticut state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Delaware":
    def de(de_income):
        if de_income <= 2000:
            return de_income * 0.00
        elif de_income <= 5000:
            return 2000 * 0.00 + (de_income - 2000) * 0.022
        elif de_income <= 10000:
            return 2000 * 0.00 + (5000 - 2000) * 0.022 + (de_income - 5000) * 0.039
        elif de_income <= 20000:
            return 2000 * 0.00 + (5000 - 2000) * 0.022 + (10000 - 5000) * 0.039 + (de_income - 10000) * 0.048
        elif de_income <= 25000:
            return 2000 * 0.00 + (5000 - 2000) * 0.022 + (10000 - 5000) * 0.039 + (20000 - 10000) * 0.048 + \
                   (de_income - 20000) * .052
        elif de_income <= 60000:
            return 2000 * 0.00 + (5000 - 2000) * 0.022 + (10000 - 5000) * 0.039 + (20000 - 10000) * 0.048 + \
                   (25000 - 20000) * .052 + (de_income - 25000) * 0.055
        else:
            return 2000 * 0.00 + (5000 - 2000) * 0.022 + (10000 - 5000) * 0.039 + (20000 - 10000) * 0.048 + \
                   (25000 - 20000) * .052 + (60000 - 25000) * 0.055 + (de_income - 60000) * 0.066



    def print_info(de, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        de_loss = de(de_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - de_loss - fica
        ret_income = income - afterTaxes - de_loss - fica - retirement
        print("Total Delaware state taxes you pay: $", round(de_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Delaware state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Florida":
    def fl(fl_income):
        return 0

    def print_info(fl_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        fl_loss = fl(fl_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - fl_loss - fica
        ret_income = income - afterTaxes - fl_loss - fica - retirement
        print("Total Florida state taxes you pay: $", round(fl_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Florida state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Georgia":
    def ga(ga_income):
        if status == "single":
            if ga_income <= 750:
                return ga_income * 0.01
            elif ga_income <= 2250:
                return 750 * 0.01 + (ga_income - 750) * 0.02
            elif ga_income <= 3750:
                return 750 * 0.01 + (2250 - 750) * 0.02 + (ga_income - 2250) * 0.03
            elif ga_income <= 5250:
                return 750 * 0.01 + (2250 - 750) * 0.02 + (3750 - 2250) * 0.03 + \
                       (ga_income - 3750) * 0.04
            elif ga_income <= 7000:
                return 750 * 0.01 + (2250 - 750) * 0.02 + (3750 - 2250) * 0.03 + \
                       (5250 - 3750) * 0.04 + (ga_income - 5250) * 0.05
            else:
                return 750 * 0.01 + (2250 - 750) * 0.02 + (3750 - 2250) * 0.03 + \
                       (5250 - 3750) * 0.04 + (7000 - 5250) * 0.05 + (ga_income - 7000) * 0.0575

        elif status == "married filed jointly":
            if ga_income <= 1000:
                return ga_income * 0.01
            elif ga_income <= 3000:
                return 1000 * 0.01 + (ga_income - 1000) * 0.02
            elif ga_income <= 5000:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (ga_income - 3000) * 0.03
            elif ga_income <= 7000:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (5000 - 3000) * 0.03 + \
                       (ga_income - 5000) * 0.04
            elif ga_income <= 10000:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (5000 - 3000) * 0.03 + \
                       (7000 - 5000) * 0.04 + (ga_income - 7000) * 0.05
            else:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (5000 - 3000) * 0.03 + \
                       (7000 - 5000) * 0.04 + (10000 - 7000) * 0.05 + (ga_income - 10000) * 0.0575

        elif status == "married filed separately":
            if ga_income <= 500:
                return ga_income * 0.01
            elif ga_income <= 1500:
                return 500 * 0.01 + (ga_income - 500) * 0.02
            elif ga_income <= 2500:
                return 500 * 0.01 + (1500 - 500) * 0.02 + (ga_income - 1500) * 0.03
            elif ga_income <= 3500:
                return 500 * 0.01 + (1500 - 500) * 0.02 + (2500 - 1500) * 0.03 + \
                       (ga_income - 2500) * 0.04
            elif ga_income <= 5000:
                return 500 * 0.01 + (1500 - 500) * 0.02 + (2500 - 1500) * 0.03 + \
                       (3500 - 2500) * 0.04 + (ga_income - 3500) * 0.05
            else:
                return 500 * 0.01 + (1500 - 500) * 0.02 + (2500 - 1500) * 0.03 + \
                       (3500 - 2500) * 0.04 + (5000 - 3500) * 0.05 + (ga_income - 5000) * 0.0575

        elif status == "head of household":
            if ga_income <= 1000:
                return ga_income * 0.01
            elif ga_income <= 3000:
                return 1000 * 0.01 + (ga_income - 1000) * 0.02
            elif ga_income <= 5000:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (ga_income - 3000) * 0.03
            elif ga_income <= 7000:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (5000 - 3000) * 0.03 + \
                       (ga_income - 5000) * 0.04
            elif ga_income <= 10000:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (5000 - 3000) * 0.03 + \
                       (7000 - 5000) * 0.04 + (ga_income - 7000) * 0.05
            else:
                return 1000 * 0.01 + (3000 - 1000) * 0.02 + (5000 - 3000) * 0.03 + \
                       (7000 - 5000) * 0.04 + (10000 - 7000) * 0.05 + (ga_income - 10000) * 0.0575

    def print_info(ga_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ga_loss = ga(ga_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ga_loss - fica
        ret_income = income - afterTaxes - ga_loss - fica - retirement
        print("Total Georgia state taxes you pay: $", round(ga_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Georgia state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Hawaii":
    def hi(hi_income):
        if status == "single":
            if hi_income <= 2400:
                return hi_income * 0.014
            elif hi_income <= 4800:
                return 2400 * 0.014 + (hi_income - 2400) * 0.032
            elif hi_income <= 9600:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (hi_income - 4800) * 0.055
            elif hi_income <= 14400:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (9600 - 4800) * 0.055 + \
                       (hi_income - 9600) * 0.064
            elif hi_income <= 19200:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (9600 - 4800) * 0.055 + \
                       (14400 - 9600) * 0.064 + (hi_income - 14400) * 0.068
            elif hi_income <= 24000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (9600 - 4800) * 0.055 + \
                        (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (hi_income - 19200) * 0.072
            elif hi_income <= 36000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                        (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                        (hi_income - 24000) * 0.076
            elif hi_income <= 48000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                        (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                        (36000 - 24000) * 0.076 + (hi_income - 36000) * 0.0790
            elif hi_income <= 150000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                        (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                        (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (hi_income - 48000) * 0.0825
            elif hi_income <= 175000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                        (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                        (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (150000 - 48000) * 0.0825 + \
                        (hi_income - 150000) * 0.09
            elif hi_income <= 200000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                        (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                        (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (150000 - 48000) * 0.0825 +\
                        (175000 - 150000) * 0.09 + (hi_income - 175000) * 0.10
            else:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                       (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                       (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (150000 - 48000) * 0.0825 +\
                        (175000 - 150000) * 0.09 + (200000 - 175000) * 0.10 + (hi_income - 200000) * 0.11


        elif status == "married filed jointly":
            if hi_income <= 4800:
                return hi_income * 0.014
            elif hi_income <= 9600:
                return 4800 * 0.014 + (hi_income - 4800) * 0.032
            elif hi_income <= 19200:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (hi_income - 9600) * 0.055
            elif hi_income <= 28800:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 9600) * 0.055 + \
                           (hi_income - 19200) * 0.064
            elif hi_income <= 38400:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 9600) * 0.055 + \
                           (28800 - 19200) * 0.064 + (hi_income - 28800) * 0.068
            elif hi_income <= 48000:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                           (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (hi_income - 38400) * 0.072
            elif hi_income <= 72000:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                        (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (48000 - 38400) * 0.072 +\
                        (hi_income - 48000) * 0.076
            elif hi_income <= 96000:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                        (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (48000 - 38400) * 0.072 +\
                        (72000 - 48000) * 0.076 + (hi_income - 72000) * 0.0790
            elif hi_income <= 300000:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                        (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (48000 - 38400) * 0.072+\
                        (72000 - 48000) * 0.076 + (96000 - 72000) * 0.0790 + (hi_income - 96000) * 0.0825
            elif hi_income <= 350000:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                        (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (48000 - 38400) * 0.072+\
                        (72000 - 48000) * 0.076 + (96000 - 72000) * 0.0790 + (300000 - 96000) * 0.0825 + \
                        (hi_income - 300000) * 0.09
            elif hi_income <= 400000:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                        (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (48000 - 38400) * 0.072 +\
                        (72000 - 48000) * 0.076 + (96000 - 72000) * 0.0790 + (300000 - 96000) * 0.0825 + \
                        (350000 - 300000) * 0.09 + (hi_income - 350000) * 0.10
            else:
                return 4800 * 0.014 + (9600 - 4800) * 0.032 + (19200 - 49600) * 0.055 + \
                        (28800 - 19200) * 0.064 + (38400 - 28800) * 0.068 + (48000 - 38400) * 0.072 +\
                        (72000 - 48000) * 0.076 + (96000 - 72000) * 0.0790 + (300000 - 96000) * 0.0825 + \
                        (350000 - 300000) * 0.09 + (400000 - 350000) * 0.10 + (hi_income - 400000) * 0.11



        elif status == "married filed separately":
            if hi_income <= 2400:
                return hi_income * 0.014
            elif hi_income <= 4800:
                return 2400 * 0.014 + (hi_income - 2400) * 0.032
            elif hi_income <= 9600:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (hi_income - 4800) * 0.055
            elif hi_income <= 14400:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (9600 - 4800) * 0.055 + \
                           (hi_income - 9600) * 0.064
            elif hi_income <= 19200:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (9600 - 4800) * 0.055 + \
                           (14400 - 9600) * 0.064 + (hi_income - 14400) * 0.068
            elif hi_income <= 24000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (9600 - 4800) * 0.055 + \
                           (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (hi_income - 19200) * 0.072
            elif hi_income <= 36000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                            (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072+\
                            (hi_income - 24000) * 0.076
            elif hi_income <= 48000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                            (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                            (36000 - 24000) * 0.076 + (hi_income - 36000) * 0.0790
            elif hi_income <= 150000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                            (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                            (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (hi_income - 48000) * 0.0825
            elif hi_income <= 175000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                            (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                            (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (150000 - 48000) * 0.0825 +\
                            (hi_income - 150000) * 0.09
            elif hi_income <= 200000:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                           (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                           (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (150000 - 48000) * 0.0825 + \
                           (175000 - 150000) * 0.09 + (hi_income - 175000) * 0.10
            else:
                return 2400 * 0.014 + (4800 - 2400) * 0.032 + (3750 - 2250) * 0.055 + \
                           (14400 - 9600) * 0.064 + (19200 - 14400) * 0.068 + (24000 - 19200) * 0.072 +\
                           (36000 - 24000) * 0.076 + (48000 - 36000) * 0.0790 + (150000 - 48000) * 0.0825 + \
                           (175000 - 150000) * 0.09 + (200000 - 175000) * 0.10 + (hi_income - 200000) * 0.11

        elif status == "head of household":
            if hi_income <= 3600:
                return hi_income * 0.014
            elif hi_income <= 7200:
                return 3600 * 0.014 + (hi_income - 3600) * 0.032
            elif hi_income <= 14400:
                return 3600 * 0.014 + (7200 - 3600) * 0.032 + (hi_income - 7200) * 0.055
            elif hi_income <= 21600:
                return 3600 * 0.014 + (7200 - 3600) * 0.032 + (14400 - 7200) * 0.055 + \
                           (hi_income - 14400) * 0.064
            elif hi_income <= 28800:
                return 3600 * 0.014 + (7200 - 3600) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (hi_income - 21600) * 0.068
            elif hi_income <= 36000:
                return 3600 * 0.014 + (7200 - 3600) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (28800 - 21600) * 0.068 + (hi_income - 28800) * 0.072
            elif hi_income <= 54000:
                return 3600 * 0.014 + (7200 - 3600) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (28800 - 21600) * 0.068 + (36000 - 28800) * 0.072 +\
                           (hi_income - 36000) * 0.076
            elif hi_income <= 72000:
                return 3600 * 0.014 + (7200 - 3600) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (28800 - 21600) * 0.068 + (36000 - 28800) * 0.072+\
                           (54000 - 36000) * 0.076 + (hi_income - 54000) * 0.0790
            elif hi_income <= 225000:
                return 3600 * 0.014 + (4800 - 2400) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (28800 - 21600) * 0.068 + (36000 - 28800) * 0.072 +\
                           (54000 - 36000) * 0.076 + (72000 - 54000) * 0.0790 + (hi_income - 72000) * 0.0825
            elif hi_income <= 262000:
                return 3600 * 0.014 + (4800 - 2400) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (19200 - 14400) * 0.068 + (36000 - 28800) * 0.072+\
                           (54000 - 36000) * 0.076 + (72000 - 54000) * 0.0790 + (225000 - 72000) * 0.0825 + \
                           (hi_income - 225000) * 0.09
            elif hi_income <= 300000:
                return 3600 * 0.014 + (4800 - 2400) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (19200 - 14400) * 0.068 + (36000 - 28800) * 0.072 +\
                           (54000 - 36000) * 0.076 + (72000 - 54000) * 0.0790 + (225000 - 72000) * 0.0825 + +\
                                   (262000 - 225000) * 0.09 + (hi_income - 262000) * 0.10
            else:
                return 3600 * 0.014 + (4800 - 2400) * 0.032 + (14400 - 7200) * 0.055 + \
                           (21600 - 14400) * 0.064 + (19200 - 14400) * 0.068 + (36000 - 28800) * 0.072+\
                           (54000 - 36000) * 0.076 + (72000 - 54000) * 0.0790 + (225000 - 72000) * 0.0825 + \
                           (262000 - 225000) * 0.09 + (300000 - 262000) * 0.10 + (hi_income - 300000) * 0.11


        def print_info(hi_income, afterTaxes):
            print("Total federal taxes you pays: $", round(afterTaxes, 2))
            hi_loss = hi(hi_income)
            ssc_tax = income * 0.062
            medi_tax = income * 0.0145
            fica = ssc_tax + medi_tax
            retirement = float(input("Enter the retirement saving amount: $"))
            final_income = income - afterTaxes - hi_loss - fica
            ret_income = income - afterTaxes - hi_loss - fica - retirement
            print("Total Hawaii state taxes you pay: $", round(hi_loss, 2))
            print("Total FICA tax deducted: $", round(fica, 2))
            print("Income after fed taxes: $", round(income - afterTaxes, 2))
            print("Income after Hawaii state taxes: $", round(final_income, 2))
            print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Idaho":
    def id(id_income):
        if status == "single":
            if id_income <= 1568:
                return id_income * 0.01125
            elif id_income <= 3136:
                return 1568 * 0.01125 + (id_income - 1568) * 0.03125
            elif id_income <= 4704:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (id_income - 3136) * 0.03625
            elif id_income <= 6272:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                       (id_income - 4704) * 0.04625
            elif id_income <= 7840:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                       (6272 - 4704) * 0.04625 + (id_income - 6272) * 0.05625
            elif id_income <= 11760:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                       (6272 - 4704) * 0.04625 + (7840 - 6272) * 0.05625 + (id_income - 7840) * 0.06625
            else:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                       (4704 - 6272) * 0.04625 + (6272 - 7840) * 0.05625 + (11760 - 7840) * 0.06625 + \
                       (id_income - 11760) * 0.06925

        elif status == "married filed jointly":
            if id_income <= 3136:
                return id_income * 0.01125
            elif id_income <= 6272:
                return 3136 * 0.01125 + (id_income - 3136) * 0.03125
            elif id_income <= 9408:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (id_income - 6272) * 0.03625
            elif id_income <= 12544:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                       (id_income - 9408) * 0.04625
            elif id_income <= 15680:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                       (12544 - 9408) * 0.04625 + (id_income - 12544) * 0.05625
            elif id_income <= 23520:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                       (12544 - 9408) * 0.04625 + (15680 - 12544) * 0.05625 + (id_income - 15680) * 0.06625
            else:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                       (12544 - 9408) * 0.04625 + (15680 - 12544) * 0.05625 + (23520 - 15680) * 0.06625 + \
                       (id_income - 23520) * 0.06925


        elif status == "married filed separately":
            if id_income <= 1568:
                return id_income * 0.01125
            elif id_income <= 3136:
                return 1568 * 0.01125 + (id_income - 1568) * 0.03125
            elif id_income <= 4704:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (id_income - 3136) * 0.03625
            elif id_income <= 6272:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                   (id_income - 4704) * 0.04625
            elif id_income <= 7840:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                   (6272 - 4704) * 0.04625 + (id_income - 6272) * 0.05625
            elif id_income <= 11760:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                   (6272 - 4704) * 0.04625 + (7840 - 6272) * 0.05625 + (id_income - 7840) * 0.06625
            else:
                return 1568 * 0.01125 + (3136 - 1568) * 0.03125 + (4704 - 3136) * 0.03625 + \
                   (4704 - 6272) * 0.04625 + (6272 - 7840) * 0.05625 + (11760 - 7840) * 0.06625 +\
                   (id_income - 11760) * 0.06925



        elif status == "head of household":
            if id_income <= 3136:
                return id_income * 0.01125

            elif id_income <= 6272:
                return 3136 * 0.01125 + (id_income - 3136) * 0.03125
            elif id_income <= 9408:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (id_income - 6272) * 0.03625
            elif id_income <= 12544:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                   (id_income - 9408) * 0.04625
            elif id_income <= 15680:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                   (12544 - 9408) * 0.04625 + (id_income - 12544) * 0.05625
            elif id_income <= 23520:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                   (12544 - 9408) * 0.04625 + (15680 - 12544) * 0.05625 + (id_income - 15680) * 0.06625
            else:
                return 3136 * 0.01125 + (6272 - 3136) * 0.03125 + (9408 - 6272) * 0.03625 + \
                   (12544 - 9408) * 0.04625 + (15680 - 12544) * 0.05625 + (23520 - 15680) * 0.06625 + \
                   (id_income - 23520) * 0.06925


    def print_info(id_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        id_loss = id(id_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - id_loss - fica
        ret_income = income - afterTaxes - id_loss - fica - retirement
        print("Total Idaho state taxes you pay: $", round(id_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Idaho state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Illinois":
    def il(il_income):
        return il_income * 0.0495

    def print_info(il, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        il_loss = il(il_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - il - fica
        ret_income = income - afterTaxes - il_loss - fica - retirement
        print("Total Illinois state taxes you pay: $", round(il_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Illinois state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Iowa":
    def ia(ia_income):
        if ia_income <= 1666:
            return ia_income * 0.033
        elif ia_income <= 3332:
            return 1666 * 0.033 + (ia_income - 1666) * 0.067
        elif ia_income <= 6664:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (ia_income - 3332) * 0.0225
        elif ia_income <= 14994:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (6664 - 3332) * 0.0225 + (14994 - 6664) * \
                   0.0414 + (ia_income - 14994) * 0.0563
        elif ia_income <= 24990:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (6664 - 3332) * 0.0225 + (14994 - 6664) * \
                   0.0414 + (24990 - 14994) * 0.0563 + (ia_income - 24990) * 0.0596
        elif ia_income <= 33320:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (6664 - 3332) * 0.0225 + (14994 - 6664) * \
                   0.0414 + (24990 - 14994) * 0.0563 + (33320 - 24990) * 0.0596 + (ia_income - 33320) * 0.0625
        elif ia_income <= 49980:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (6664 - 3332) * 0.0225 + (14994 - 6664) * \
                   0.0414 + (24990 - 14994) * 0.0563 + (33320 - 24990) * 0.0596 + (49980 - 33320) * 0.0625 +\
                   (ia_income - 49980) * 0.0744
        elif ia_income <= 74970:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (6664 - 3332) * 0.0225 + (14994 - 6664) *\
                   0.0414 + (24990 - 14994) * 0.0563 + (33320 - 24990) * 0.0596 + (49980 - 33320)\
                   * 0.0625 + (74970 - 49980) * 0.0744
        else:
            return 1666 * 0.033 + (3332 - 1666) * 0.067 + (6664 - 3332) * 0.0225 +(14994 - 6664) *\
                   0.0414 + (24990 - 14994) * 0.0563 + (33320 - 24990) * 0.0596 + (49980 - 33320) *\
                   0.0625 + (74970 - 49980) * 0.0744 + (ia_income - 74970) * 0.0853


    def print_info(ia_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ia_loss = ia(ia_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ia_loss - fica
        ret_income = income - afterTaxes - ia_loss - fica - retirement
        print("Total Iowa state taxes you pay: $", round(ia_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Iowa state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Indiana":
    def IN(IN_income):
        return IN_income * 0.0323


    def print_info(in_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        IN_loss = IN(IN_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - IN_loss - fica
        ret_income = income - afterTaxes - IN_loss - fica - retirement
        print("Total Indiana state taxes you pay: $", round(IN_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Indiana state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Kentucky":
    def ky(ky_income):
        return ky_income * 0.05

    def print_info(ky_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ky_loss = ky(ky_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ky_loss - fica
        ret_income = income - afterTaxes - ky_loss - fica - retirement
        print("Total Kentucky state taxes you pay: $", round(ky_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Kentucky state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Louisiana":
    def la(la_income):
        if status == "single":
            if la_income <= 12500:
                return la_income * 0.02
            elif la_income <= 50000:
                return 12500 * 0.02 + (la_income - 12500) * 0.04
            else:
                return 12500 * 0.02 + (50000 - 12500) * 0.04 + (la_income - 50000) * 0.06

        elif status == "married filed jointly":
            if la_income <= 25000:
                return la_income * 0.02
            elif la_income <= 100000:
                return 25000 * 0.02 + (la_income - 25000) * 0.04
            else:
                return 25000 * 0.02 + (100000 - 25000) * 0.04 + (la_income - 100000) * 0.06

        elif status == "married filed separately":
            if la_income <= 12500:
                return la_income * 0.02
            elif la_income <= 50000:
                return 15000 * 0.02 + (la_income - 12500) * 0.04
            else:
                return 15000 * 0.02 + (50000 - 12500) * 0.04 + (la_income - 50000) * 0.06

        elif status == "head of household":
            if la_income <= 12500:
                return la_income * 0.02
            elif la_income <= 50000:
                return 15000 * 0.02 + (la_income - 12500) * 0.04
            else:
                return 15000 * 0.02 + (50000 - 12500) * 0.04 + (la_income - 50000) * 0.06


    def print_info(la_income, afterTaxes):
            print("Total federal taxes you pays: $", round(afterTaxes, 2))
            la_loss = la(la_income)
            ssc_tax = income * 0.062
            medi_tax = income * 0.0145
            fica = ssc_tax + medi_tax
            retirement = float(input("Enter the retirement saving amount: $"))
            final_income = income - afterTaxes - la_loss - fica
            ret_income = income - afterTaxes - la_loss - fica - retirement
            print("Total Louisiana state taxes you pay: $", round(la_loss, 2))
            print("Total FICA tax deducted: $", round(fica, 2))
            print("Income after fed taxes: $", round(income - afterTaxes, 2))
            print("Income after Louisiana state taxes: $", round(final_income, 2))
            print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Maine":
    def me(me_income):
        if status == "single":
            if me_income <= 22000:
                return me_income * 0.580
            elif me_income <= 52600:
                return 22000 * 0.580 + (me_income - 22000) * 0.675
            else:
                return 22000 * 0.580 + (52600 - 22000) * 0.675 + (me_income - 52600) * 0.715

        elif status == "married filed jointly":
            if me_income <= 44500:
                return me_income * 0.580
            elif me_income <= 105200:
                return 44500 * 0.580 + (me_income - 44500) * 0.675
            else:
                return 44500 * 0.580 + (105200 - 44500) * 0.675 + (me_income - 105200) * 0.715

        elif status == "married filed separately":
            if me_income <= 22000:
                return me_income * 0.580
            elif me_income <= 52600:
                return 22000 * 0.580 + (me_income - 22000) * 0.675
            else:
                return 22000 * 0.580 + (52600 - 22000) * 0.675 + (me_income - 52600) * 0.715

        elif status == "head of household":
            if me_income <= 33300:
                return me_income * 0.580
            elif me_income <= 78900:
                return 33300 * 0.580 + (me_income - 33300) * 0.675
            else:
                return 33300 * 0.580 + (78900 - 33300) * 0.675 + (me_income - 78900) * 0.715

    def print_info(me, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        me_loss = me(me_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - me_loss - fica
        ret_income = income - afterTaxes - me_loss - fica - retirement
        print("Total Maine state taxes you pay: $", round(me_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Maine state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Maryland":
    def md(md_income):
        if status == "single":
            if md_income <= 1000:
                return md_income * 0.02
            elif md_income <= 2000:
                return 1000 * 0.02 + (md_income - 1000) * 0.03
            elif md_income <= 3000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (md_income - 2000) * 0.04
            elif md_income <= 100000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (md_income - 3000) * 0.0475
            elif md_income <= 125000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (100000 - 3000) * 0.0475 + (md_income - 100000) * 0.05
            elif md_income <= 150000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (100000 - 3000) * 0.0475 + (125000 - 100000) * 0.05 + (md_income - 125000)* 0.0525
            elif md_income <= 250000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                        (100000 - 3000) * 0.0475 + (125000 - 100000) * 0.05 + (150000 - 125000)* 0.0525 + (md_income - 150000)* 0.055
            else:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (100000 - 3000) * 0.0475 + (125000 - 100000) * 0.05 + (150000 - 125000) * 0.0525 + (25000 - 150000) * 0.055 +(md_income - 250000) * 0.0575

        elif status == "married filed jointly":
            if md_income <= 1000:
                return md_income * 0.02
            elif md_income <= 2000:
                return 1000 * 0.02 + (md_income - 1000) * 0.03
            elif md_income <= 3000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (md_income - 2000) * 0.04
            elif md_income <= 150000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (md_income - 3000) * 0.0475
            elif md_income <= 175000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (150000 - 3000) * 0.0475 + (md_income - 150000) * 0.05
            elif md_income <= 225000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (150000 - 3000) * 0.0475 + (175000 - 150000) * 0.05 + (md_income - 175000)* 0.0525
            elif md_income <= 300000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                        (150000 - 3000) * 0.0475 + (175000 - 150000) * 0.05 + (225000 - 175000)* 0.0525 + (md_income - 225000)* 0.055
            else:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (150000 - 3000) * 0.0475 + (175000 - 150000) * 0.05 + (225000 - 175000) * 0.0525 + (300000 - 225000) * 0.055 +(md_income - 300000) * 0.0575


        elif status == "married filed separately":
            if md_income <= 1000:
                return md_income * 0.02
            elif md_income <= 2000:
                return 1000 * 0.02 + (md_income - 1000) * 0.03
            elif md_income <= 3000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (md_income - 2000) * 0.04
            elif md_income <= 100000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (md_income - 3000) * 0.0475
            elif md_income <= 125000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (100000 - 3000) * 0.0475 + (md_income - 100000) * 0.05
            elif md_income <= 150000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (100000 - 3000) * 0.0475 + (125000 - 100000) * 0.05 + (md_income - 125000)* 0.0525
            elif md_income <= 250000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                        (100000 - 3000) * 0.0475 + (125000 - 100000) * 0.05 + (150000 - 125000)* 0.0525 + (md_income - 150000)* 0.055
            else:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (100000 - 3000) * 0.0475 + (125000 - 100000) * 0.05 + (150000 - 125000) * 0.0525 + (25000 - 150000) * 0.055 +(md_income - 250000) * 0.0575
        elif status == "head of household":
            if md_income <= 1000:
                return md_income * 0.02
            elif md_income <= 2000:
                return 1000 * 0.02 + (md_income - 1000) * 0.03
            elif md_income <= 3000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (md_income - 2000) * 0.04
            elif md_income <= 150000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (md_income - 3000) * 0.0475
            elif md_income <= 175000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (150000 - 3000) * 0.0475 + (md_income - 150000) * 0.05
            elif md_income <= 225000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (150000 - 3000) * 0.0475 + (175000 - 150000) * 0.05 + (md_income - 175000)* 0.0525
            elif md_income <= 300000:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                        (150000 - 3000) * 0.0475 + (175000 - 150000) * 0.05 + (225000 - 175000)* 0.0525 + (md_income - 225000)* 0.055
            else:
                return 1000 * 0.02 + (2000 - 1000) * 0.03 + (3000 - 2000) * 0.04 + \
                       (150000 - 3000) * 0.0475 + (175000 - 150000) * 0.05 + (225000 - 175000) * 0.0525 + (300000 - 225000) * 0.055 +(md_income - 300000) * 0.0575

    def print_info(md, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        md_loss = md(md_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - md_loss - fica
        ret_income = income - afterTaxes - md_loss - fica - retirement
        print("Total Maryland state taxes you pay: $", round(md_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Maryland state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Massachusetts":
    def ma(ma_income):
        return ma_income * 0.050

    def print_info(ma_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ma_loss = ma(ma_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ma_loss - fica
        ret_income = income - afterTaxes - ma_loss - fica - retirement
        print("Total Massachusetts state taxes you pay: $", round(ma_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Massachusetts state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Michigan":
    def mi(mi_income):
        return mi_income * 0.0425

    def print_info(mi_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        mi_loss = mi(mi_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - mi_loss - fica
        ret_income = income - afterTaxes - mi_loss - fica - retirement
        print("Total Michigan state taxes you pay: $", round(mi_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Michigan state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Minnesota":
    def mn(mn_income):
        if status == "single":
            if mn_income <= 26960:
                return mn_income * 0.0535
            elif mn_income <= 88550:
                return 26960 * 0.0535 + (mn_income - 26960) * 0.0680
            elif mn_income <= 164400:
                return 26960 * 0.0535 + (88550 - 26960) * 0.0535 + (mn_income - 16440) * 0.0785
            else:
                return 26960 * 0.0535 + (88550 - 26960) * 0.0535 + (164400 - 88550) * 0.0785 + \
                       (mn_income - 164400) * 0.0985

        elif status == "married filed jointly":
            if mn_income <= 39140:
                return mn_income * 0.0535
            elif mn_income <= 156570:
                return 39140 * 0.0535 + (mn_income - 39140) * 0.0680
            elif mn_income <= 273470:
                return 39140 * 0.0535 + (156570 - 39140) * 0.0680 + (mn_income - 156570) * 0.0785
            else:
                return 39140 * 0.0535 + (156570 - 39140) * 0.068 - + (273470 - 156570) * 0.0785 + \
                       (mn_income - 156570) * 0.0985

        elif status == "married filed separately":
            if mn_income <= 19705:
                return mn_income * 0.0535
            elif mn_income <= 78285:
                return 19705 * 0.0535 + (mn_income - 19705) * 0.0680
            elif mn_income <= 136735:
                return 19705 * 0.0535 + (78285 - 19705) * 0.0680 + (mn_income - 136735) * 0.0785
            else:
                return 19705 * 0.0535 + (78285 - 19705) * 0.0680 + (136735 - 78285) * 0.0785 + \
                       (mn_income - 136735) * 0.0985

        elif status == "head of household":
            if mn_income <= 33190:
                return mn_income * 0.0535
            elif mn_income <= 133360:
                return 33190 * 0.0535 + (mn_income - 33190) * 0.0680
            elif mn_income <= 218540:
                return 33190 * 0.0535 + (133360 - 33190) * 0.0680 + (mn_income - 218540) * 0.0785
            else:
                return 33190 * 0.0535 + (133360 - 33190) * 0.0680 + (218540 - 133360) * 0.0785 + \
                       (mn_income - 218540) * 0.0985

    def print_info(mn_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        mn_loss = mn(mn_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - mn_loss - fica
        ret_income = income - afterTaxes - mn_loss - fica - retirement
        print("Total Minnesota state taxes you pay: $", round(mn_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Minnesota state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Mississippi":
    def ms(ms_income):
        if ms_income <= 2000:
            return ms_income * 0.00
        elif ms_income <= 5000:
            return 2000 * 0.00 + (ms_income - 2000) * 0.03
        elif ms_income <= 10000:
            return 2000 * 0.00 + (5000 - 2000) * 0.03 + (ms_income - 10000) * 0.04
        else:
            return 2000 * 0.00 + (5000 - 2000) * 0.03 + (10000 - 5000) * 0.04 + \
                   (ms_income - 10000) * 0.05

    def print_info(ms_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ms_loss = ms(ms_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ms_loss - fica
        ret_income = income - afterTaxes - ms_loss - fica - retirement
        print("Total Mississippi state taxes you pay: $", round(ms_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Mississippi state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Missouri":
    def mo(mo_income):
        if mo_income <= 107:
            return mo_income * 0.00
        elif mo_income <= 1073:
            return 107 * 0.00 + (mo_income - 107) * 0.015
        elif mo_income <= 2146:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (mo_income - 1073) * 0.020
        elif mo_income <= 3219:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (mo_income - 2146) * 0.025
        elif mo_income <= 4292:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (3219 - 2146) * 0.025 + \
                   (mo_income - 3219) * .030
        elif mo_income <= 5365:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (3219 - 2146) * 0.025 + \
                   (4292 - 3219) * .030 + (mo_income - 4292) * 0.035
        elif mo_income <= 6438:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (3219 - 2146) * 0.025 + \
                   (4292 - 3219) * .030 + (5365 - 4292) * 0.035 + (mo_income - 5365) * 0.040
        elif mo_income <= 7511:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (3219 - 2146) * 0.025 + \
                   (4292 - 3219) * .030 + (5365 - 4292) * 0.035 + (6438 - 5365) * 0.040 + (mo_income - 6438) * 0.045
        elif mo_income <= 8484:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (3219 - 2146) * 0.025 + \
                   (4292 - 3219) * .030 + (5365 - 4292) * 0.035 + (6438 - 5365) * 0.040 + (7511 - 6438) * 0.045 + \
                   (mo_income - 7511) * 0.050
        else:
            return 107 * 0.00 + (1073 - 107) * 0.015 + (2146 - 1073) * 0.020 + (3219 - 2146) * 0.025 + \
                   (4292 - 3219) * .030 + (5365 - 4292) * 0.035 + (6438 - 5365) * 0.040 + (7511 - 6438) * 0.045 + \
                   (8784 - 7511) * 0.050 + (mo_income - 8484) * 0.054

    def print_info(mo_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        mos_loss = mo(mo_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - mo_loss - fica
        ret_income = income - afterTaxes - mo_loss - fica - retirement
        print("Total Missouri state taxes you pay: $", round(mo_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Missouri state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Montana":
    def mt(mt_income):
        if mt_income <= 3100:
            return mt_income * 0.01
        elif mt_income <= 5400:
            return 3100 * 0.01 + (mt_income - 3100) * 0.02
        elif mt_income <= 8200:
            return 3100 * 0.01 + (5400 - 3100) * 0.02 + (mt_income - 5400) * 0.03
        elif mt_income <= 11100:
            return 3100 * 0.01 + (5400 - 3100) * 0.02 + (8200 - 5400) * 0.03 + (mt_income - 8200) * 0.04
        elif mt_income <= 14300:
            return 3100 * 0.01 + (5400 - 3100) * 0.02 + (8200 - 5400) * 0.03 + (11100 - 8200) * 0.04 + (mt_income - 11100) * 0.05
        elif mt_income <= 18400:
            return 3100 * 0.01 + (5400 - 3100) * 0.02 + (8200 - 5400) * 0.03 + (11100 - 8200) * 0.04 + (14300 - 11100) * 0.05 + (mt_income - 14300) * 0.06
        else:
            return 3100 * 0.01 + (5400 - 3100) * 0.02 + (8200 - 5400) * 0.03 + (11100 - 8200) * 0.04 + (14300 - 11100) * 0.05 + (18400 - 14300) * 0.06 + \
            (mt_income - 18400) * 0.069

    def print_info(mt, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        mt_loss = mt(mt_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - mt_loss - fica
        ret_income = income - afterTaxes - mt_loss - fica - retirement
        print("Total Montana state taxes you pay: $", round(mt_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Montana state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "New Jersey":
    def nj(nj_income):
        if status == "single":
            if nj_income <= 20000:
                return nj_income * 0.01400
            elif nj_income <= 35000:
                return 20000 * 0.01400 + (nj_income - 20000) * 0.01750
            elif nj_income <= 40000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.01750 + (nj_income - 35000) * 0.0350
            elif nj_income <= 75000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.01750 + (40000 - 35000) * 0.0350 + \
                       (nj_income - 40000) * 0.05525
            elif nj_income <= 500000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.01750 + (40000 - 35000) * 0.0350 + \
                       (500000 - 75000) * 0.05525 + (nj_income - 75000) * 0.06370
            elif nj_income <= 5000000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.01750 + (40000 - 35000) * 0.0350 + \
                       (500000 - 75000) * 0.05525 + (500000 - 75000) * 0.06370 + (nj_income - 500000) * 0.08970
            else:
                return 20000 * 0.01400 + (35000 - 20000) * 0.01750 + (40000 - 35000) * 0.0350 + \
                       (500000 - 75000) * 0.05525 + (500000 - 75000) * 0.06370 + (5000000 - 500000) * 0.08970 + (nj_income - 5000000) * 0.10750

        elif status == "married filed jointly":
            if nj_income <= 20000:
                return nj_income * 0.01400
            elif nj_income <= 50000:
                return 20000 * 0.01400 + (nj_income - 20000) * 0.01750
            elif nj_income <= 70000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (nj_income - 50000) * 0.02450
            elif nj_income <= 80000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (nj_income - 70000) * 0.03500
            elif nj_income <= 150000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (nj_income - 80000) * 0.05525
            elif nj_income <= 500000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (150000 - 80000) * 0.05525 + (nj_income - 150000) * 0.06370
            elif nj_income <= 5000000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (150000 - 80000) * 0.05525 + (500000 - 150000) * 0.06370 + (nj_income - 500000) * 0.08970
            else:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (150000 - 80000) * 0.05525 + (500000 - 150000) * 0.06370 + (5000000 - 500000) * 0.08970 + (nj_income - 5000000) * 0.10750

        elif status == "married filed separately":
            if nj_income <= 20000:
                return nj_income * 0.01400
            elif nj_income <= 35000:
                return 20000 * 0.01400 + (nj_income - 20000) * 0.017500
            elif nj_income <= 40000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.017500 + (nj_income - 35000) * 0.0350
            elif nj_income <= 75000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.017500 + (40000 - 350000) * 0.0350 + \
                       (nj_income - 40000) * 0.05525
            elif nj_income <= 500000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.017500 + (40000 - 35000) * 0.0350 + \
                       (75000 - 40000) * 0.05525 + (nj_income - 40000) * 0.06370
            elif nj_income <= 5000000:
                return 20000 * 0.01400 + (35000 - 20000) * 0.017500 + (40000 - 35000) * 0.0350 + \
                       (75000 - 40000) * 0.05525 + (500000 - 75000) * 0.06370 + (nj_income - 5000000) * 0.08970
            else:
                return 20000 * 0.01400 + (35000 - 20000) * 0.017500 + (40000 - 35000) * 0.0350 + \
                       (75000 - 40000) * 0.05525 + (500000 - 75000) * 0.06370 + (500000 - 5000000) * 0.06370 + (5000000 - 500000) * 0.08970 + (nj_income - 5000000) * 0.10750

        elif status == "head of household":
            if nj_income <= 20000:
                return nj_income * 0.01400
            elif nj_income <= 50000:
                return 20000 * 0.01400 + (nj_income - 20000) * 0.01750
            elif nj_income <= 70000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (nj_income - 50000) * 0.02450
            elif nj_income <= 80000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (nj_income - 70000) * 0.03500
            elif nj_income <= 150000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (nj_income - 80000) * 0.05525
            elif nj_income <= 500000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (150000 - 80000) * .05525 + (nj_income - 150000) * 0.06370
            elif nj_income <= 5000000:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (150000 - 80000) * .05525 + (500000 - 150000) * 0.06370 + (nj_income - 500000) * 0.08970
            else:
                return 20000 * 0.01400 + (50000 - 20000) * 0.01750 + (70000 - 50000) * 0.02450 + \
                       (80000 - 70000) * 0.03500 + (150000 - 80000) * 0.05525 + (500000 - 150000) * 0.06370 + (5000000 - 500000) * 0.08970 + (nj_income - 5000000) * 0.10750

    def print_info(nj_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        nj_loss = nj(nj_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - nj_loss - fica
        ret_income = income - afterTaxes - nj_loss - fica - retirement
        print("Total New Jersey state taxes you pay: $", round(nj_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after New Jersey state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "New Mexico":
    def nm(nm_income):
        if status == "single":
            if nm_income <= 5500:
                return nm_income * 0.017
            elif nm_income <= 11000:
                return 5500 * 0.017 + (nm_income - 5500) * 0.032
            elif nm_income <= 16000:
                return 5500 * 0.017 + (11000 - 5500) * 0.032 + (nm_income - 11000) * 0.047

            else:
               return 5500 * 0.017 + (11000 - 5500) * 0.032 + (16000 - 11000) * 0.047+(nm_income - 16000) * 0.049


        elif status == "married filed jointly":
            if nm_income <= 8000:
                return nm_income * 0.017
            elif nm_income <= 16000:
                return 8000 * 0.017 + (nm_income - 8000) * 0.032
            elif nm_income <= 24000:
                return 8000 * 0.017 + (16000 - 8000) * 0.032 + (nm_income - 16000) * 0.047

            else:
               return 8000 * 0.017 + (16000 - 8000) * 0.032 + (24000 - 16000) * 0.047+(nm_income - 24000) * 0.049


        elif status == "married filed separately":
            if nm_income <= 4000:
                return nm_income * 0.017
            elif nm_income <= 8000:
                return 4000 * 0.017 + (nm_income - 4000) * 0.032
            elif nm_income <= 12000:
                return 4000 * 0.017 + (8000 - 4000) * 0.032 + (nm_income - 8000) * 0.047

            else:
               return 4000 * 0.017 + (8000 - 4000) * 0.032 + (12000 - 8000) * 0.047+(nm_income - 12000) * 0.049

        elif status == "head of household":
            if nm_income <= 8000:
                return nm_income * 0.017
            elif nm_income <= 16000:
                return 8000 * 0.017 + (nm_income - 8000) * 0.032
            elif nm_income <= 24000:
                return 8000 * 0.017 + (16000 - 8000) * 0.032 + (nm_income - 16000) * 0.047

            else:
               return 8000 * 0.017 + (16000 - 8000) * 0.032 + (24000 - 16000) * 0.047+(nm_income -  24000) * 0.049

    def print_info(nm_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        nm_loss = fl(nm_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - nm_loss - fica
        ret_income = income - afterTaxes - nm_loss - fica - retirement
        print("Total New Mexico state taxes you pay: $", round(nm_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after New Mexico state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "New York":
    def ny(ny_income):
        if status == "single":
            if ny_income <= 8500:
                return ny_income * 0.04
            elif ny_income <= 11700:
                return 8500 * 0.04 + (ny_income - 8500) * 0.045
            elif ny_income <= 13900:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (ny_income - 11700) * 0.0525
            elif ny_income <= 21400:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (ny_income - 13900) * 0.059
            elif ny_income <= 80650:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (21400 - 13900) * 0.059 + (ny_income - 21400) * 0.0609
            elif ny_income <= 215400:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (21400 - 13900) * 0.059 + (80650 - 21400) * 0.0609 + (ny_income - 80650) * 0.0641
            elif ny_income <= 1077550:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (21400 - 13900) * 0.059 + (80650 - 21400) * 0.0609 + (215400 - 80650) * 0.0641 + (ny_income - 215400) * 0.0685

            else:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                	(21400 - 13900) * 0.059 + (80650 - 21400) * 0.0609 + (215400 - 80650) * 0.0641 + (1077550 - 215400) * 0.0685 + (ny_income - 1077550) * 0.0882


        elif status == "married filed jointly":
            if ny_income <= 17150:
                return ny_income * 0.04
            elif ny_income <= 23600:
                return 17150 * 0.04 + (ny_income - 8500) * 0.045
            elif ny_income <= 27900:
                return 17150 * 0.04 + (23600 - 17150) * 0.045 + (ny_income - 23600) * 0.0525
            elif ny_income <= 43000:
                return 17150 * 0.04 + (23600 - 17150) * 0.045 + (27900 - 23600) * 0.0525 + \
                       (ny_income - 27900) * 0.059
            elif ny_income <= 161550:
                return 17150 * 0.04 + (23600 - 17150) * 0.045 + (27900 - 23600) * 0.0525 + \
                       (43000 - 27900) * 0.059 + (ny_income - 43000) * 0.0609
            elif ny_income <= 323200:
                return 17150 * 0.04 + (23600 - 17150) * 0.045 + (27900 - 23600) * 0.0525 + \
                       (43000 - 27900) * 0.059 + (161550 - 43000) * 0.0609 + (ny_income - 161550) * 0.0641
            elif ny_income <= 2155350:
                return 17150 * 0.04 + (23600 - 17150) * 0.045 + (27900 - 23600) * 0.0525 + \
                       (43000 - 27900) * 0.059 + (161550 - 43000) * 0.0609 + (323200 - 161550) * 0.0641 + (ny_income - 323200) * 0.0641


            else:
                return 17150 * 0.04 + (23600 - 17150) * 0.045 + (27900 - 23600) * 0.0525 + \
                       (43000 - 27900) * 0.059 + (161550 - 43000) * 0.0609 + (323200 - 161550) * 0.0641 + (2155350 - 323200) * 0.0641 + (ny_income - 2155350) * 0.0641


        elif status == "married filed separately":
            if ny_income <= 8500:
                return ny_income * 0.04
            elif ny_income <= 11700:
                return 8500 * 0.04 + (ny_income - 8500) * 0.045
            elif ny_income <= 13900:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (ny_income - 11700) * 0.0525
            elif ny_income <= 21400:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (ny_income - 13900) * 0.059
            elif ny_income <= 80650:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (21400 - 13900) * 0.059 + (ny_income - 21400) * 0.0609
            elif ny_income <= 215400:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (21400 - 13900) * 0.059 + (80650 - 21400) * 0.0609 + (ny_income - 80650) * 0.0641
            elif ny_income <= 1077550:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                       (21400 - 13900) * 0.059 + (80650 - 21400) * 0.0609 + (215400 - 80650) * 0.0641 + (ny_income - 215400) * 0.0685

            else:
                return 8500 * 0.04 + (11700 - 8500) * 0.045 + (13900 - 11700) * 0.0525 + \
                	(21400 - 13900) * 0.059 + (80650 - 21400) * 0.0609 + (215400 - 80650) * 0.0641 + (1077550 - 215400) * 0.0685 + (ny_income - 1077550) * 0.0882

        elif status == "head of household":
            if ny_income <= 12800:
                return ny_income * 0.04
            elif ny_income <= 17650:
                return 12800 * 0.04 + (ny_income - 12800) * 0.045
            elif ny_income <= 20900:
                return 12800 * 0.04 + (17650 - 12800) * 0.045 + (ny_income - 17650) * 0.0525
            elif ny_income <= 32200:
                return 12800 * 0.04 + (17650 - 12800) * 0.045 + (20900 - 17650) * 0.0525 + \
                       (ny_income - 20900) * 0.059
            elif ny_income <= 107650:
                return 12800 * 0.04 + (17650 - 12800) * 0.045 + (20900 - 17650) * 0.0525 + \
                       (32200 - 20900) * 0.059 + (ny_income - 32200) * 0.0609
            elif ny_income <= 269300:
                return 12800 * 0.04 + (17650 - 12800) * 0.045 + (20900 - 17650) * 0.0525 + \
                       (32200 - 20900) * 0.059 + (107650 - 32200) * 0.0609 + (ny_income - 107650) * 0.0641
            elif ny_income <= 1616450:
                return 12800 * 0.04 + (17650 - 12800) * 0.045 + (20900 - 17650) * 0.0525 + \
                       (32200 - 20900) * 0.059 + (107650 - 32200) * 0.0609 + (269300 - 107650) * 0.0641 + (ny_income - 269300) * 0.0685

            else:
                return 12800 * 0.04 + (17650 - 12800) * 0.045 + (20900 - 17650) * 0.0525 + \
                       (32200 - 20900) * 0.059 + (107650 - 32200) * 0.0609 + (269300 - 107650) * 0.0641 + (1616450 - 269300) * 0.0685 + (ny_income - 1616450) * 0.0882


    def print_info(ny_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ny_loss = ny(ny_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ny_loss - fica
        ret_income = income - afterTaxes - ny_loss - fica - retirement
        print("Total New York state taxes you pay: $", round(ny_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after New York state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "North Carolina":
    def nc(nc_income):
        return nc_income * 0.0525


    def print_info(nc_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        nc_loss = nc(nc_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - nc_loss - fica
        ret_income = income - afterTaxes - nc_loss - fica - retirement
        print("Total North Carolina state taxes you pay: $", round(nc_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after North Carolina state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "North Dakota":
    def nd(nd_income):
        if status == "single":
            if nd_income <= 40125:
                return nd_income * 0.011
            elif nd_income <= 97150:
                return 40125 * 0.011 + (nd_income - 40125) * 0.0204
            elif nd_income <= 202650:
                return 40125 * 0.011 + (97150 - 40125) * 0.0204 + (nd_income - 97150) * 0.0227
            elif nd_income <= 440600:
                return 40125 * 0.011 + (97150 - 40125) * 0.0204 + (202650 - 97150) * 0.0227 + \
                       (nd_income - 202650) * 0.0264
            else:
                return 40125 * 0.011 + (97150 - 40125) * 0.0204 + (202650 - 97150) * 0.0227 + \
                       (440600 - 202650) * 0.0264 +  (nd_income - 440600) * 0.029

        elif status == "married filed jointly":
            if nd_income <= 67050:
                return nd_income * 0.011
            elif nd_income <= 161950:
                return 67050 * 0.011 + (nd_income - 67050) * 0.0204
            elif nd_income <= 246700:
                return 67050 * 0.011 + (161950 - 67050) * 0.0204 + (nd_income - 161950) * 0.0227
            elif nd_income <= 440600:
                return 67050 * 0.011 + (161950 - 67050) * 0.0204 + (246700 - 161950) * 0.0227 + \
                       (nd_income - 246700) * 0.0264
            else:
                 return 67050 * 0.011 + (161950 - 67050) * 0.0204 + (246700 - 161950) * 0.0227 + \
                       (nd_income - 246700) * 0.0264 +  (nd_income - 440600) * 0.029

        elif status == "married filed separately":
            if nd_income <= 33525:
                return nd_income * 0.011
            elif nd_income <= 80975:
                return 33525 * 0.011 + (nd_income - 33525) * 0.0204
            elif nd_income <= 123350:
                return 33525 * 0.011 + (80975 - 33525) * 0.0204 + (nd_income - 80975) * 0.0227
            elif nd_income <= 220300:
                return 33525 * 0.011 + (80975 - 33525) * 0.0204 + (123350 - 80975) * 0.0227 + \
                       (nd_income - 123350) * 0.0264
            else:
                 return 33525 * 0.011 + (80975 - 33525) * 0.0204 + (123350 - 80975) * 0.0227 + \
                       (nd_income - 123350) * 0.0264 +  (nd_income - 220300) * 0.029

        elif status == "head of household":
            if nd_income <= 53750:
                return nd_income * 0.011
            elif nd_income <= 138800:
                return 53750 * 0.011 + (nd_income - 53750) * 0.0204
            elif nd_income <= 224700:
                return 53750 * 0.011 + (138800 - 53750) * 0.0204 + (nd_income - 138800) * 0.0227
            elif nd_income <= 440600:
                return 53750 * 0.011 + (138800 - 53750) * 0.0204 + (224700 - 138800) * 0.0227 + \
                       (nd_income - 224700) * 0.0264
            else:
                 return 53750 * 0.011 + (138800 - 53750) * 0.0204 + (224700 - 138800) * 0.0227 + \
                       (nd_income - 224700) * 0.0264 +  (nd_income - 440600) * 0.029

    def print_info(nd_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        nd_loss = nd(nd_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - nd_loss - fica
        ret_income = income - afterTaxes - nd_loss - fica - retirement
        print("Total North Dakota state taxes you pay: $", round(nd_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after North Dakota state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Ohio":
    def oh(oh_income):
        if oh_income <= 22150:
            return oh_income * 0.00
        elif oh_income <= 44250:
            return 22150 * 0.00 + (oh_income - 22150) * 0.0285
        elif oh_income <= 88450:
            return 22150 * 0.00 + (44250 - 22150) * 0.0285 + (oh_income - 44250) * 0.03326
        elif oh_income <= 110650:
            return 22150 * 0.00 + (44250 - 22150) * 0.0285 + (88450 - 44250) * 0.03326 + (oh_income - 88450) * 0.03802
        elif oh_income <= 221300:
            return 22150 * 0.00 + (44250 - 22150) * 0.0285 + (88450 - 44250) * 0.03326 + (110650 - 88450) * 0.03802 + (oh_income - 110650) * 0.04413

        else:
            return 22450 * 0.00 + (44250 - 22150) * 0.0285 + (88450 - 44250) * 0.03326 + (110650 - 88450) * 0.03802 + (221300 - 110650) * 0.04413 + (oh_income - 2241300) * 0.04797

    def print_info(oh_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        oh_loss = oh(oh_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - oh_loss - fica
        ret_income = income - afterTaxes - oh_loss - fica - retirement
        print("Total Ohio state taxes you pay: $", round(oh_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Ohio state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "South Dakota":
    def sd(sd_income):
        return 0


    def print_info(sd_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        sd_loss = sd(sd_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - sd_loss - fica
        ret_income = income - afterTaxes - sd_loss - fica - retirement
        print("Total South Dakota state taxes you pay: $", round(sd_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after South Dakota state taxes: $", round(final_income, 2))


elif state == "Tennessee":
    def tn(tn_income):
        return 0


    def print_info(tn_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        tn_loss = tn(tn_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - tn_loss - fica
        ret_income = income - afterTaxes - tn_loss - fica - retirement
        print("Total Tennessee state taxes you pay: $", round(tn_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Tennessee state taxes: $", round(final_income, 2))



elif state == "Texas":
    def tx(tx_income):
        return 0


    def print_info(tx_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        tx_loss = tx(tx_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - tx_loss - fica
        ret_income = income - afterTaxes - tx_loss - fica - retirement
        print("Total Texas state taxes you pay: $", round(tx_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Texas state taxes: $", round(final_income, 2))



elif state == "Nebraska":
    def ne(ne_income):
        if status == "single":
            if ne_income <= 3290:
                return ne_income * 0.0246
            elif ne_income <= 19700:
                return 3290 * 0.0246 + (ne_income - 3290) * 0.0351
            elif ne_income <= 31750:
                return 3290 * 0.0246 + (19700 - 3290) * 0.0351 + (ne_income - 19700) * 0.0501
            else:
                return 3290 * 0.0246 + (19700 - 3290) * 0.0351 + (31750 - 19700) * 0.0501 + \
                       (ne_income - 31750) * 0.0684

        elif status == "married filed jointly":
            if ne_income <= 6570:
                return ne_income * 0.0246
            elif ne_income <= 39410:
                return 6570 * 0.0246 + (ne_income - 6570) * 0.0351
            elif ne_income <= 63500:
                return 6570 * 0.0246 + (39410 - 6570) * 0.0351 + (ne_income - 39410) * 0.0501
            else:
                return 6570 * 0.0246 + (39410 - 6570) * 0.0351 + (63500 - 39410) * 0.0501 + \
                       (ne_income - 63500) * 0.0684

        elif status == "married filed separately":
            if ne_income <= 3290:
                return ne_income * 0.0246
            elif ne_income <= 19700:
                return 3290 * 0.0246 + (ne_income - 3290) * 0.0351
            elif ne_income <= 31750:
                return 3290 * 0.0246 + (19700 - 3290) * 0.0351 + (ne_income - 19700) * 0.0501
            else:
                return 3290 * 0.0246 + (19700 - 3290) * 0.0351 + (31750 - 19700) * 0.0501 + \
                       (ne_income - 31750) * 0.0684

        elif status == "head of household":
            if ne_income <= 6130:
                return ne_income * 0.0246
            elif ne_income <= 31530:
                return 6130 * 0.0246 + (ne_income - 6130) * 0.0351
            elif ne_income <= 47080:
                return 6130 * 0.0246 + (31530 - 6130) * 0.0351 + (ne_income - 31530) * 0.0501
            else:
                return 6130 * 0.0246 + (31530 - 6130) * 0.0351 + (47080 - 31530) * 0.0501 + \
                       (ne_income - 47080) * 0.0684

    def print_info(ne_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ne_loss = ne(ne_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ne_loss - fica
        ret_income = income - afterTaxes - ne_loss - fica - retirement
        print("Total Nebraska state taxes you pay: $", round(ne_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Nebraska state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Nevada":
    def nv(nv_income):
        return 0


    def print_info(nv_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        nv_loss = nv(nv_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - nv_loss - fica
        ret_income = income - afterTaxes - nv_loss - fica - retirement
        print("Total Nevada state taxes you pay: $", round(nv_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Nevada state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "New Hampshire":
    def nh(nh_income):
        return 0


    def print_info(nh_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        nh_loss = nh(nh_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - nh_loss - fica
        ret_income = income - afterTaxes - nh_loss - fica - retirement
        print("Total New Hampshire state taxes you pay: $", round(nh_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after New Hampshire state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Oklahoma":
    def ok(ok_income):
        if status == "single":
            if ok_income <= 1000:
                return ok_income * 0.005
            elif ok_income <= 2500:
                return 1000 * 0.005 + (ok_income - 1000) * 0.01
            elif ok_income <= 3750:
                return 1000 * 0.005 + (2500 - 1000) * 0.01 + (ok_income - 2500) * 0.02
            elif ok_income <= 4900:
                return 1000 * 0.005 + (2500 - 1000) * 0.01 + (3750 - 2500) * 0.02 + \
                       (ok_income - 3750) * 0.03
            elif ok_income <= 7200:
                return 1000 * 0.005 + (2500 - 1000) * 0.01 + (3750 - 2500) * 0.02 + \
                       (4900 - 3750) * 0.03 + (ok_income - 4900) * 0.04
            else:
                 return 1000 * 0.005 + (2500 - 1000) * 0.01 + (3750 - 2500) * 0.02 + \
                       (4900 - 3750) * 0.03 + (7200 - 4900) * 0.04 + (ok_income - 7200) * 0.05


        elif status == "married filed jointly":
            if ok_income <= 2000:
                return ok_income * 0.005
            elif ok_income <= 5000:
                return 2000 * 0.005 + (ok_income - 2000) * 0.01
            elif ok_income <= 7500:
                return 2000 * 0.005 + (5000 - 2000) * 0.01 + (ok_income - 5000) * 0.02
            elif ok_income <= 9800:
                return 2000 * 0.005 + (5000 - 2000) * 0.01 + (7500 - 5000) * 0.02 + \
                       (ok_income - 7500) * 0.03
            elif ok_income <= 12200:
                return 2000 * 0.005 + (5000 - 2000) * 0.01 + (7500 - 5000) * 0.02 + \
                       (9800 -7500) * 0.03 + (ok_income - 9800) * 0.04
            else:
                 return 2000 * 0.005 + (5000 - 2000) * 0.01 + (7500 - 5000) * 0.02 + \
                       (9800 -7500) * 0.03 + (12200 - 9800) * 0.04 + (ok_income - 12200) * 0.05


        elif status == "married filed separately":
            if ok_income <= 1000:
                return ok_income * 0.005
            elif ok_income <= 2500:
                return 1000 * 0.005 + (ok_income - 1000) * 0.01
            elif ok_income <= 3750:
                return 1000 * 0.005 + (2500 - 1000) * 0.01 + (ok_income - 2500) * 0.02
            elif ok_income <= 4900:
                return 1000 * 0.005 + (2500 - 1000) * 0.01 + (3750 - 2500) * 0.02 + \
                       (ok_income - 3750) * 0.03
            elif ok_income <= 7200:
                return 1000 * 0.005 + (2500 - 1000) * 0.01 + (3750 - 2500) * 0.02 + \
                       (4900 - 3750) * 0.03 + (ok_income - 4900) * 0.04
            else:
                 return 1000 * 0.005 + (2500 - 1000) * 0.01 + (3750 - 2500) * 0.02 + \
                       (4900 - 3750) * 0.03 + (7200 - 4900) * 0.04 + (ok_income - 7200) * 0.05

        elif status == "head of household":
            if ok_income <= 2000:
                return ok_income * 0.005
            elif ok_income <= 5000:
                return 2000 * 0.005 + (ok_income - 2000) * 0.01
            elif ok_income <= 7500:
                return 2000 * 0.005 + (5000 - 2000) * 0.01 + (ok_income - 5000) * 0.02
            elif ok_income <= 9800:
                return 2000 * 0.005 + (5000 - 2000) * 0.01 + (7500 - 5000) * 0.02 + \
                       (ok_income - 7500) * 0.03
            elif ok_income <= 12200:
                return 2000 * 0.005 + (5000 - 2000) * 0.01 + (7500 - 5000) * 0.02 + \
                       (9800 -7500) * 0.03 + (ok_income - 9800) * 0.04
            else:
                 return 2000 * 0.005 + (5000 - 2000) * 0.01 + (7500 - 5000) * 0.02 + \
                       (9800 -7500) * 0.03 + (12200 - 9800) * 0.04 + (ok_income - 12200) * 0.05


    def print_info(ok_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ok_loss = ok(ok_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ok_loss - fica
        ret_income = income - afterTaxes - ok_loss - fica - retirement
        print("Total Oklahoma state taxes you pay: $", round(ok_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Oklahoma state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Oregon":
    def OR(or_income):
        if status == "single":
            if or_income <= 3600:
                return or_income * 0.0475
            elif or_income <= 9050:
                return 3600 * 0.0475 + (or_income - 3600) * 0.0675
            elif or_income <= 125000:
                return 3600 * 0.0475 + (9050 - 3600) * 0.0675 + (or_income - 9050) * 0.0875

            else:
                 return 3600 * 0.0475 + (9050 - 3600) * 0.0675 + (125000 - 9050) * 0.0875 + (or_income - 125000) * 0.099


        elif status == "married filed jointly":
            if or_income <= 7200:
                return or_income * 0.0475
            elif or_income <= 18100:
                return 7200 * 0.0475 + (or_income - 7200) * 0.0675
            elif or_income <= 250000:
                return 7200 * 0.0475 + (18100 - 7200) * 0.0675 + (or_income - 18100) * 0.0875
            else:
                 return 7200 * 0.0475 + (18100 - 7200) * 0.0675 + (250000 - 18100) * 0.0875 + (or_income - 250000) * 0.099


        elif status == "married filed separately":
            if or_income <= 3600:
                return or_income * 0.0475
            elif or_income <= 9050:
                return 3600 * 0.0475 + (or_income - 3600) * 0.0675
            elif or_income <= 125000:
                return 3600 * 0.0475 + (9050 - 3600) * 0.0675 + (or_income - 9050) * 0.0875

            else:
                 return 3600 * 0.0475 + (9050 - 3600) * 0.0675 + (125000 - 9050) * 0.0875 + (or_income - 125000) * 0.099


        elif status == "head of household":
            if or_income <= 7200:
                return or_income * 0.0475
            elif or_income <= 18100:
                return 7200 * 0.0475 + (or_income - 7200) * 0.0675
            elif or_income <= 250000:
                return 7200 * 0.0475 + (18100 - 7200) * 0.0675 + (or_income - 18100) * 0.0875
            else:
                 return 7200 * 0.0475 + (18100 - 7200) * 0.0675 + (250000 - 18100) * 0.0875 + (or_income - 250000) * 0.099


    def print_info(OR_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        OR_loss = OR(OR_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - OR_loss - fica
        ret_income = income - afterTaxes - OR_loss - fica - retirement
        print("Total Oregon state taxes you pay: $", round(or_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Oregon state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))

elif state == "Pennsylvania":
    def pa(pa_income):
        return pa_income * 0.0307


    def print_info(pa_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        pa_loss = pa(pa_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - pa_loss - fica
        ret_income = income - afterTaxes - pa_loss - fica - retirement
        print("Total Pennsylvania state taxes you pay: $", round(pa_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Pennsylvania state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))



elif state == "Rhode Island":
    def ri(ri_income):
        if ri_income <= 65250:
            return ri_income * 0.0375
        elif ri_income <= 148350:
            return 65250 * 0.0375 + (ri_income - 65250) * 0.0475
        else:
            return 65250 * 0.0375 + (148350 - 65250) * 0.0475 + (ri_income - 148350) * 0.0599

    def print_info(ri_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        ri_loss = ri(ri_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ri_loss - fica
        ret_income = income - afterTaxes - ri_loss - fica - retirement
        print("Total Rhode Island state taxes you pay: $", round(ri_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Rhode Island state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "South Carolina":
    def sc(sc_income):
        if sc_income <= 3070:
            return sc_income * 0
        elif sc_income <= 6150:
            return 3070 * 0 + (sc_income - 3070) * 0.03
        elif sc_income <= 9230:
            return 3070 * 0 + (6150 - 3070) * 0.03 + (sc_income - 6150) * 0.04
        elif sc_income <= 12310:
            return 3070 * 0 + (6150 - 3070) * 0.03 + (9230 - 6150) * 0.04 + (sc_income - 9230) * 0.05
        elif sc_income <= 15400:
            return 3070 * 0 + (6150 - 3070) * 0.03 + (9230 - 6150) * 0.04 + (12310 - 9230) * 0.05 + (sc_income - 12310) * 0.06

        else:
            return 3070 * 0 + (6150 - 3070) * 0.03 + (9230 - 6150) * 0.04 + (12310 - 9230) * 0.05 + (15400 - 12310) * 0.06 + (sc_income - 15400) * 0.07

    def print_info(sc_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        sc_loss = sc(sc_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - sc_loss - fica
        ret_income = income - afterTaxes - sc_loss - fica - retirement
        print("Total South Carolina state taxes you pay: $", round(sc_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - aftertaxes, 2))
        print("Income after South Carolina state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Kansas":
    def ks(ks_income):
        if status == "single":
            if ks_income <= 15000:
                return ks_income * 0.310
            elif ks_income <= 30000:
                return 15000 * 0.310 + (ks_income - 15000) * 0.525
            else:
                return 15000 * 0.310 + (30000 - 15000) * 0.525 + (ks_income - 30000) * 0.570

        elif status == "married filed jointly":
            if ks_income <= 30000:
                return ks_income * 0.310
            elif ks_income <= 60000:
                return 30000 * 0.310 + (ks_income - 30000) * 0.525
            else:
                return 30000 * 0.310 + (60000 - 30000) * 0.525 + (ks_income - 60000) * 0.570

        elif status == "married filed separately":
            if ks_income <= 15000:
                return ks_income * 0.310
            elif ks_income <= 30000:
                return 15000 * 0.310 + (ks_income - 15000) * 0.525
            else:
                return 15000 * 0.310 + (30000 - 15000) * 0.525 + (ks_income - 30000) * 0.570

        elif status == "head of household":
            if ks_income <= 15000:
                return ks_income * 0.310
            elif ks_income <= 30000:
                return 15000 * 0.310 + (ks_income - 30000) * 0.525
            else:
                return 15000 * 0.310 + (30000 - 15000) * 0.525 + (ks_income - 30000) * 0.570

    def print_info(ks_income, afterTaxes):
        print("Total federal taxes you pays: $", round(fedTaxes_paid, 2))
        ks_loss = ks(ks_income)
        final_income = income - fedTaxes_paid - ks_loss
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - ks_loss - fica
        ret_income = income - afterTaxes - ks_loss - fica - retirement
        print("Total Kansas state taxes you pay: $", round(ks_loss, 2))
        print("Income after fed taxes: $", round(income - fedTaxes_paid, 2))
        print("Income after Kansas state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Washington":
    def wa(wa_income):
        return 0


    def print_info(wa_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        wa_loss = wa(wa_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        final_income = income - afterTaxes - wa_loss - fica
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - fl_loss - fica
        ret_income = income - afterTaxes - fl_loss - fica - retirement
        print("Total Washington state taxes you pay: $", round(wa_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Washington state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Utah":
    def ut(ut_income):
        return ut_income * 0.045


    def print_info(ut_income, afterTaxes):
        print("Total federal taxes you pays: $", round(fedTaxes_paid, 2))
        ut_loss = ut(ut_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - fl_loss - fica
        ret_income = income - afterTaxes - fl_loss - fica - retirement
        print("Total Utah state taxes you pay: $", round(ut_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Utah state taxes: $", round(final_income, 2))


elif state == "Vermont":
    def vt(vt_income):
        if status == "single":
            if vt_income <= 40350:
                return vt_income * 0.0335
            elif vt_income <= 97800:
                return 40350 * 0.0335 + (vt_income - 40350) * 0.0660
            elif vt_income <= 204000:
                return 40350 * 0.0335 + (97800 - 40350) * 0.0660 + (vt_income - 97800) * 0.0760
            else:
                return 40350 * 0.0335 + (97800 - 40350) * 0.0660 + (204000 - 97800) * 0.0760 + \
                       (vt_income - 204000) * 0.0875

        elif status == "married filed jointly":
            if vt_income <= 67450:
                return vt_income * 0.0335
            elif vt_income <= 163000:
                return 67450 * 0.0335 + (vt_income - 67450) * 0.0660
            elif vt_income <= 248350:
                return 67450 * 0.0335 + (163000 - 67450) * 0.0660 + (vt_income - 163000) * 0.0760
            else:
                return 67450 * 0.0335 + (163000 - 67450) * 0.0660 + (248350 - 163000) * 0.0760 + \
                       (vt_income - 248350) * 0.0875

        elif status == "married filed separately":
            if vt_income <= 33725:
                return vt_income * 0.0335
            elif vt_income <= 81500:
                return 33725 * 0.0335 + (vt_income - 33725) * 0.0660
            elif vt_income <= 124175:
                return 33725 * 0.0335 + (81500 - 33725) * 0.0660 + (vt_income - 81500) * 0.0760
            else:
                return 33725 * 0.0335 + (81500 - 33725) * 0.0660 + (124175 - 81500) * 0.0760 + \
                       (vt_income - 124175) * 0.0875

        elif status == "head of household":
            if vt_income <= 54100:
                return vt_income * 0.0335
            elif vt_income <= 139650:
                return 54100 * 0.0335 + (vt_income - 54100) * 0.0660
            elif vt_income <= 226200:
                return 54100 * 0.0335 + (139650 - 54100) * 0.0660 + (vt_income - 139650) * 0.0760
            else:
                return 54100 * 0.0335 + (139650 - 54100) * 0.0660 + (226200 - 139650) * 0.0760 + \
                       (vt_income - 226200) * 0.0875

    def print_info(vt_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        vt_loss = vt(vt_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - fl_loss - fica
        ret_income = income - afterTaxes - fl_loss - fica - retirement
        print("Total Vermont state taxes you pay: $", round(vt_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Vermont state taxes: $", round(final_income, 2))


elif state == "Virginia":
    def va(va_income):
        if va_income <= 3000:
            return va_income * 0.02
        elif va_income <= 5000:
            return 3000 * 0.02 + (va_income - 3000) * 0.03
        elif va_income <= 17000:
            return 3000 * 0.02 + (5000 - 3000) * 0.03 + (va_income - 5000) * 0.05
        else:
            return 3000 * 0.02 + (5000 - 3000) * 0.03 + (17000 - 5000) * 0.05 + \
               (va_income - 17000) * 0.0575

    def print_info(va_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        va_loss = va(va_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - va_loss - fica
        ret_income = income - afterTaxes - va_loss - fica - retirement
        print("Total Virginia state taxes you pay: $", round(va_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Virginia state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "West Virginia":
    def wv(wv_income):
        if status == "single":
            if wv_income <= 10000:
                return wv_income * 0.03
            elif wv_income <= 25000:
                return 10000 * 0.01 + (wv_income - 10000) * 0.04
            elif wv_income <= 40000:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (wv_income - 25000) * 0.0450
            elif wv_income <= 60000:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (40000 - 25000) * 0.0450 + \
                       (wv_income - 40000) * 0.06
            else:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (40000 - 25000) * 0.0450 + \
                       (60000 - 40000) * 0.06 + (wv_income - 60000) * 0.0650

        elif status == "married filed jointly":
            if wv_income <= 10000:
                return wv_income * 0.03
            elif wv_income <= 25000:
                return 10000 * 0.01 + (wv_income - 10000) * 0.04
            elif wv_income <= 40000:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (wv_income - 25000) * 0.0450
            elif wv_income <= 60000:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (40000 - 25000) * 0.0450 + \
                       (wv_income - 40000) * 0.06
            else:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (40000 - 25000) * 0.0450 + \
                       (60000 - 40000) * 0.06 + (wv_income - 60000) * 0.0650

        elif status == "married filed separately":
            if wv_income <= 5000:
                return wv_income * 0.03
            elif wv_income <= 12500:
                return 5000 * 0.01 + (wv_income - 5000) * 0.04
            elif wv_income <= 20000:
                return 5000 * 0.01 + (12500 - 5000) * 0.04 + (wv_income - 12500) * 0.0450
            elif wv_income <= 30000:
                return 5000 * 0.01 + (12500 - 5000) * 0.04 + (20000 - 12500) * 0.0450 + \
                       (wv_income - 20000) * 0.06
            else:
                return 5000 * 0.01 + (12500 - 5000) * 0.04 + (20000 - 12500) * 0.0450 + \
                       (30000 - 20000) * 0.06 + (wv_income - 30000) * 0.0650

        elif status == "head of household":
            if wv_income <= 10000:
                return wv_income * 0.03
            elif wv_income <= 25000:
                return 10000 * 0.01 + (wv_income - 10000) * 0.04
            elif wv_income <= 40000:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (wv_income - 25000) * 0.0450
            elif wv_income <= 60000:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (40000 - 25000) * 0.0450 + \
                       (wv_income - 40000) * 0.06
            else:
                return 10000 * 0.01 + (25000 - 10000) * 0.04 + (40000 - 25000) * 0.0450 + \
                       (60000 - 40000) * 0.06 + (wv_income - 60000) * 0.0650


    def print_info(wv_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        wv_loss = wv(wv_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        final_income = income - afterTaxes - wv_loss - fica
        print("Total West Virginia state taxes you pay: $", round(wv_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after West Virginia state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


elif state == "Wisconsin":
    def wi(wi_income):
        if status == "single":
            if wi_income <= 11790:
                return wi_income * 0.0354
            elif wi_income <= 23930:
                return 11790 * 0.0354 + (wi_income - 11790) * 0.0465
            elif wi_income <= 263480:
                return 11790 * 0.0354 + (23930 - 11790) * 0.0465 + (wi_income - 23930) * 0.0627
            else:
                return 11790 * 0.0354 + (23930 - 11790) * 0.0465 + (263480 - 23930) * 0.0627 + \
                       (wi_income - 263480) * 0.0765

        elif status == "married filed jointly":
            if wi_income <= 15960:
                return wi_income * 0.0354
            elif wi_income <= 31910:
                return 15960 * 0.0354 + (wi_income - 15960) * 0.0465
            elif wi_income <= 351310:
                return 15960 * 0.0354 + (31910 - 15960) * 0.0465 + (wi_income - 31910) * 0.0627
            else:
                return 15960 * 0.0354 + (31910 - 15960) * 0.0465 + (263480 - 31910) * 0.0627 + \
                       (wi_income - 351310) * 0.0765

        elif status == "married filed separately":
            if wi_income <= 7980:
                return wi_income * 0.0354
            elif wi_income <= 15960:
                return 7980 * 0.0354 + (wi_income - 7980) * 0.0465
            elif wi_income <= 175660:
                return 7980 * 0.0354 + (15960 - 7980) * 0.0465 + (wi_income - 15960) * 0.0627
            else:
                return 7980 * 0.0354 + (15960 - 7980) * 0.0465 + (175660 - 15960) * 0.0627 + \
                       (wi_income - 175660) * 0.0765

        elif status == "head of household":
            if wi_income <= 11790:
                return wi_income * 0.0354
            elif wi_income <= 23930:
                return 11790 * 0.0354 + (wi_income - 11790) * 0.0465
            elif wi_income <= 263480:
                return 11790 * 0.0354 + (23930 - 11790) * 0.0465 + (wi_income - 23930) * 0.0627
            else:
                return 11790 * 0.0354 + (23930 - 11790) * 0.0465 + (263480 - 23930) * 0.0627 + \
                       (wi_income - 263480) * 0.0765

    def print_info(wi_income, afterTaxes):
        print("Total federal taxes you pays: $", round(fedTaxes_paid, 2))
        wi_loss = wi(wi_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - wi_loss - fica
        ret_income = income - afterTaxes - wi_loss - fica - retirement
        print("Total Wisconsin state taxes you pay: $", round(wi_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Wisconsin state taxes: $", round(final_income, 2))


elif state == "Wyoming":
    def wy(wy_income):
        return 0


    def print_info(wy_income, afterTaxes):
        print("Total federal taxes you pays: $", round(afterTaxes, 2))
        wy_loss = fl(wy_income)
        ssc_tax = income * 0.062
        medi_tax = income * 0.0145
        fica = ssc_tax + medi_tax
        retirement = float(input("Enter the retirement saving amount: $"))
        final_income = income - afterTaxes - wy_loss - fica
        ret_income = income - afterTaxes - wy_loss - fica - retirement
        print("Total Wyoming state taxes you pay: $", round(wy_loss, 2))
        print("Total FICA tax deducted: $", round(fica, 2))
        print("Income after fed taxes: $", round(income - afterTaxes, 2))
        print("Income after Wyoming state taxes: $", round(final_income, 2))
        print("Income after retirement saving: $", round(ret_income, 2))


def federal():
    global state
    global status
    global income
    if status == "single":
        if str(int(income)) == "0":
           sys.exit()
        elif income <= 9875:
            afterTaxes = income * 0.10
            print_info(income,afterTaxes)
        elif income <= 40125:
            afterTaxes = 9875 * 0.10 + (income - 9875) * 0.12
            print_info(income,afterTaxes)
        elif income <= 85525:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (income - 40125) * 0.22
            print_info(income,afterTaxes)
        elif income <= 163300:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (income - 85525) * 0.24
            print_info(income,afterTaxes)
        elif income <= 207350:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (163300 - 85525) * 0.24 + (income - 163300) * 0.32
            print_info(income,afterTaxes)
        elif income <= 518400:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (163300 - 85525) * 0.24 + (207350 - 163300) * 0.32 + (income - 207350) * 0.35
            print_info(income,afterTaxes)
        else:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (163300 - 85525) * 0.24 + (207350 - 163300) * 0.32 + (518400 - 207350) * 0.35 + \
                         (income - 518400) * 0.37
            print_info(income,afterTaxes)


    elif status == "married filed jointly":

        if str(int(income)) == "0":
           sys.exit()
        elif income <= 19750:
            afterTaxes = income * 0.10
            print_info(income,afterTaxes)
        elif income <= 80250:
            afterTaxes = 19750 * 0.10 + (income - 19750) * 0.12
            print_info(income,afterTaxes)
        elif income <= 171050:
            afterTaxes = 19750 * 0.10 + (80250 - 19750) * 0.12 + (income - 80250) * 0.22
            print_info(income,afterTaxes)
        elif income <= 326600:
            afterTaxes = 19750 * 0.10 + (80250 - 19750) * 0.12 + (171050 - 80250) * 0.22 + \
                         (income - 171050) * 0.24
            print_info(income,afterTaxes)
        elif income <= 414700:
            afterTaxes = 19750 * 0.10 + (80250 - 19750) * 0.12 + (171050 - 80250) * 0.22 + \
                         (326600 - 171050) * 0.24 + (income - 326600) * 0.32
            print_info(income,afterTaxes)
        elif income <= 622050:
            afterTaxes = 19750 * 0.10 + (80250 - 19750) * 0.12 + (171050 - 80250) * 0.22 + \
                         (326600 - 171050) * 0.24 + (414700 - 326600) * 0.32 + (income - 414700) * 0.35
            print_info(income,afterTaxes)
        else:
            afterTaxes = 19750 * 0.10 + (80250 - 19750) * 0.12 + (171050 - 80250) * 0.22 + \
                         (326600 - 171050) * 0.24 + (414700 - 326600) * 0.32 + (518400 - 414700) * 0.35 + \
                         (income - 622050) * 0.37
            print_info(income,afterTaxes)


    elif status == "married filed separately":
        if str(int(income)) == "0":
           sys.exit()
        elif income <= 9875:
            afterTaxes = income * 0.10
            print_info(income,afterTaxes)
        elif income <= 40125:
            afterTaxes = 9875 * 0.10 + (income - 9875) * 0.12
            print_info(income,afterTaxes)
        elif income <= 85525:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (income - 40125) * 0.22
            print_info(income,afterTaxes)
        elif income <= 163300:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (income - 171050) * 0.24
            print_info(income,afterTaxes)
        elif income <= 207350:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (163300 - 85525) * 0.24 + (income - 163300) * 0.32
            print_info(income,afterTaxes)
        elif income <= 311025:
            afterTaxes = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + \
                         (163300 - 85525) * 0.24 + (207350 - 163300) * 0.32 + (income - 207350) * 0.35
            print_info(income,afterTaxes)
        else:
            afterTaxes = 9875 * 0.10 + (40125 - 19750) * 0.12 + (85525 - 40125) * 0.22 + \
                         (163300 - 85525) * 0.24 + (207350 - 163300) * 0.32 + (311025 - 207350) * 0.35 + \
                         (income - 311025) * 0.37
            print_info(income,afterTaxes)


    elif status == "head of household":
        if str(int(income)) == "0":
           sys.exit()
        elif income <= 14100:
            afterTaxes = income * 0.10
            print_info(income,afterTaxes)
        elif income <= 53700:
            afterTaxes = 14100 * 0.10 + (income - 14100) * 0.12
            print_info(income,afterTaxes)
        elif income <= 85500:
            afterTaxes = 14100 * 0.10 + (53700 - 14100) * 0.12 + (income - 53700) * 0.22
            print_info(income,afterTaxes)
        elif income <= 163300:
            afterTaxes = 14100 * 0.10 + (53700 - 14100) * 0.12 + (85500 - 53700) * 0.22 + \
                         (income - 85500) * 0.24
            print_info(income,afterTaxes)
        elif income <= 207350:
            afterTaxes = 14100 * 0.10 + (53700 - 14100) * 0.12 + (85500 - 53700) * 0.22 + \
                         (163300 - 85500) * 0.24 + (income - 163300) * 0.32
            print_info(income,afterTaxes)
        elif income <= 518400:
            afterTaxes = 14100 * 0.10 + (53700 - 14100) * 0.12 + (85500 - 53700) * 0.22 + \
                         (163300 - 85500) * 0.24 + (207350 - 163300) * 0.32 + (income - 207350) * 0.35
            print_info(income,afterTaxes)
        else:
            afterTaxes = 14100 * 0.10 + (53700 - 14100) * 0.12 + (85500 - 53700) * 0.22 + \
                         (163300 - 85500) * 0.24 + (207350 - 163300) * 0.32 + (518400 - 207350) * 0.35 + \
                         (income - 518400) * 0.37
            print_info(income,afterTaxes)

federal()
