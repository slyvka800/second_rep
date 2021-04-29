package iot.ua;

import lombok.Builder;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Builder
public class TablewareManager {
    private List<PackageOfDisposableTableware> items = new ArrayList<>();

    public List<PackageOfDisposableTableware> searchByMaterial(Material material)
    {
        List<PackageOfDisposableTableware> arrayOfFounds = new ArrayList<>();
        for(PackageOfDisposableTableware item: items) {
            if(item.getMaterial() == material) {
                arrayOfFounds.add(item);
            }
        }
        return arrayOfFounds;
    }

    public void sortByPrice(List<PackageOfDisposableTableware> items, SortOrder order)
    {
        if(order == SortOrder.ASC) {
            items.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second)->
                    (int)(first.getPrice() - second.getPrice()));
        } else {
            items.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second)->
                    (int)(second.getPrice() - first.getPrice()));
        }
    }

    public void sortByDate(List<PackageOfDisposableTableware> items, SortOrder order)
    {
        items.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) -> {
            int[] firstInt = first.getDateOfManufacture();
            int[] secondInt = second.getDateOfManufacture();
            StringBuilder firstStrBuilder = new StringBuilder();
            StringBuilder secondStrBuilder = new StringBuilder();

            firstStrBuilder.append(firstInt[0]).append("-").append(firstInt[1]).append("-").append(firstInt[2]);
            secondStrBuilder.append(secondInt[0]).append("-").append(secondInt[1]).append("-").append(secondInt[2]);

            String firstStr = firstStrBuilder.toString();
            String secondStr = secondStrBuilder.toString();

            SimpleDateFormat objSDF = new SimpleDateFormat("dd-MM-yyyy");
            try {
                Date dt_1 = objSDF.parse(firstStr);

                try {
                    Date dt_2 = objSDF.parse(secondStr);
                    if(order == SortOrder.ASC) {
                        return dt_1.compareTo(dt_2);
                    } else {
                        return dt_2.compareTo(dt_1);
                    }
                } catch (ParseException e) {
                    e.printStackTrace();
                }

            } catch (ParseException e) {
                e.printStackTrace();
            }
            return 0;
        });
    }
}
