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

    private void sortBy(List<PackageOfDisposableTableware> itemsForSort, SortOrder order,
                             Comparator<PackageOfDisposableTableware> comparator) {
        if (order == SortOrder.ASC) {
            itemsForSort.sort(comparator);
        } else {
            itemsForSort.sort(comparator.reversed());
        }
    }

    public void sortByPrice(List<PackageOfDisposableTableware> itemsForSort, SortOrder order) {
        sortBy(itemsForSort, order, Comparator.comparing(PackageOfDisposableTableware::getPrice));
    }

    public void sortByDate(List<PackageOfDisposableTableware> itemsForSort, SortOrder order) {
        sortBy(itemsForSort, order, Comparator.comparing(PackageOfDisposableTableware::getDateOfManufacture));
    }
}
