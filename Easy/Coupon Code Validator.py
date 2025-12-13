class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = 'electronics,grocery,pharmacy,restaurant'
        valid_coupons = []
        for i in range(len(code)):
            coupon = code[i]
            category = businessLine[i]
            active = isActive[i]
            if coupon and re.match(r'^[a-zA-Z0-9_]+$', coupon) and category in categories and active:
                valid_coupons.append((category, coupon))
        valid_coupons.sort()
        return [coupon for _, coupon in valid_coupons]
