from sheets import getSheet

def main():
    values = getSheet('1BNJKDTg_-c84h5BpSOkJTQOL4axuxCPB-rLaCbHAcfg', 'db!A2:J500000')
    sku_dict = {}
    for row in values:
        sku = int(row[0])
        unit_sale = float(row[5])
        week = int(row[8])
        store = row[9]
        if sku not in sku_dict:
            sku_dict.setdefault(sku, {})
        if week not in sku_dict[sku]:
            sku_dict[sku].setdefault(week, {})
        if store not in sku_dict[sku][week]:
            sku_dict[sku][week].setdefault(store, unit_sale)

        accumulator = sku_dict[sku][week][store]
        sku_dict[sku][week][store] = (accumulator + unit_sale) / 2
        
    print(sku_dict)

if __name__ == '__main__':
    main()