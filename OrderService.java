package ua.lviv.iot.shopping_project.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.context.annotation.ApplicationScope;
import ua.lviv.iot.shopping_project.dal.OrderRepository;
import ua.lviv.iot.shopping_project.exceptions.OrderNotFoundException;
import ua.lviv.iot.shopping_project.models.Order;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

@Service
@ApplicationScope
public class OrderService {

    private AtomicInteger id = new AtomicInteger(0);

    private Map<Integer, Order> ordersMap = new HashMap<Integer, Order>();

    @Autowired
    private OrderRepository repository;

    public Order addOrder(Order order) {

        return repository.save(order);
//        Integer orderId = id.incrementAndGet();
//        order.setId(orderId);
//        ordersMap.put(orderId, order);
//        return order;
    }

    public List<Order> getOrders() {
//        return new ArrayList<>(ordersMap.values());
        return repository.findAll();
    }

    public Order getOrder(Integer id) {
//        return ordersMap.get(id);
        return repository.findById(id).orElseThrow();
    }

    public Order updateOrder(Order order) throws OrderNotFoundException {
//        return ordersMap.put(order.getId(), order);
        if (repository.existsById(order.getId())) {
            return repository.save(order);
        }
        throw  new OrderNotFoundException("Order with id" + order.getId() + "not found");
    }
}

