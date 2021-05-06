package iot.ua;

import lombok.Builder;

import java.util.ArrayList;
import java.util.List;

@Builder
public class TablewareManager{
    private final List<PackageOfDisposableTableware> items;

    public List<PackageOfDisposableTableware> searchByMaterial(Material material)
    {
        List<PackageOfDisposableTableware> arrayOfFounds = new ArrayList<>();
        for(PackageOfDisposableTableware item: items) {
            if (item.getMaterial() == material) {
                arrayOfFounds.add(item);
            }
        }
        return arrayOfFounds;
    }

    public void sortByPrice(List<PackageOfDisposableTableware> itemsForSort, SortOrder order)
    {
        if(order == SortOrder.ASC) {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second)->
                    (int)(first.getPrice() - second.getPrice()));
        } else {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second)->
                    (int)(second.getPrice() - first.getPrice()));
        }
    }

    public void sortByDate(List<PackageOfDisposableTableware> itemsForSort, SortOrder order) {
        if(order == SortOrder.ASC)
        {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) ->
                    first.getDateOfManufacture().compareTo(second.getDateOfManufacture()));
        } else {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) ->
                    second.getDateOfManufacture().compareTo(first.getDateOfManufacture()));
        }

    }
}
