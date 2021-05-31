package ua.lviv.iot.disposable_tableware.models;

import lombok.Builder;

import java.util.List;
import java.util.stream.Collectors;

@Builder
public class TablewareManager {
    private final List<PackageOfDisposableTableware> items;

    public List<PackageOfDisposableTableware> searchByMaterial(Material material) {
        List<PackageOfDisposableTableware> founds = items.stream()
                .filter(item -> material.equals(item.getMaterial())).collect(Collectors.toList());
        return founds;
    }

    public void sortByPrice(List<PackageOfDisposableTableware> itemsForSort, SortOrder order) {
        if (order == SortOrder.ASC) {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) ->
                    (int) (first.getPrice() - second.getPrice()));
        } else {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) ->
                    (int) (second.getPrice() - first.getPrice()));
        }
    }

    public void sortByDate(List<PackageOfDisposableTableware> itemsForSort, SortOrder order) {
        if (order == SortOrder.ASC) {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) ->
                    first.getDateOfManufacture().compareTo(second.getDateOfManufacture()));
        } else {
            itemsForSort.sort((PackageOfDisposableTableware first, PackageOfDisposableTableware second) ->
                    second.getDateOfManufacture().compareTo(first.getDateOfManufacture()));
        }

    }
}
