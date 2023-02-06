class ROI():
    def __init__(self):
        self.value = []
        ROI.income(self)
    def income(self):
        inc = input("What is your monthly income? ")
        self.value.append(float(inc))
        ROI.monthlyExpenses(self)



    def monthlyExpenses(self):
        tax = input("How much Tax will you pay? ")
        self.value.append(float(tax))
        ins = input("How much is your insurance? ")
        self.value.append(float(ins))
        uti = input("How much is the utility bill? ")
        self.value.append(float(uti))
        hoa = input("How much will HOA cost? ")
        self.value.append(float(hoa))
        ls = input("How much for lawn and snow removal care? ")
        self.value.append(float(ls))
        vac = input("How much estimated for Vacancy? ")
        self.value.append(float(vac))
        rep = input("How much will you put aside for repair cost? ")
        self.value.append(float(rep))
        capx = input("How much are you setting aside for big repairs? ")
        self.value.append(float(capx))
        prop_manage = input("How much for property management? ")
        self.value.append(float(prop_manage))
        mortgage = input("Whats the mortgage cost? ")
        self.value.append(float(mortgage))
        ROI.downPayment(self)
    


    def downPayment(self):
        dp = input("What was your downpayment? ")
        self.value.append(float(dp))
        cc = input("What was the closing costs? ")
        self.value.append(float(cc))
        rb = input("What was the Rehab Budget? ")
        self.value.append(float(rb))
        misc = input("Are there any other misc expenses? ")
        self.value.append(float(misc))

        x = 0
        y = 0
        for i in range(len(self.value)):
            if i <= 3:
                x += self.value[i]
            elif i <= 13:
                x -= self.value[i]
            elif i == 14:
                x = x*12
                y += self.value[i]
            else:
                y += self.value[i]
        print("The ROI for this property is:", 100*(x/y), "%")
money = ROI()

                







