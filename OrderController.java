package ua.lviv.iot.shopping_project.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ua.lviv.iot.shopping_project.exceptions.OrderNotFoundException;
import ua.lviv.iot.shopping_project.models.Order;
import ua.lviv.iot.shopping_project.service.OrderService;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.logging.Logger;

@RestController
@RequestMapping(path = "/order")
public class OrderController {

    private static final Logger LOGGER = Logger.getLogger("ua.lviv.iot.shopping_project.controller.OrderController");

    @Autowired
    private OrderService orderService;

    @GetMapping(path = "/{id}")
    public ResponseEntity<Order> getOrder(@PathVariable(name = "id") Integer id) {
        try {
            return new ResponseEntity<Order>(orderService.getOrder(id), HttpStatus.OK);
        } catch (NoSuchElementException e) {
            LOGGER.severe("Can`t update an order with non-existing id" + id);
            return new ResponseEntity<Order>(HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping
    public List<Order> getOrders() {
        return orderService.getOrders();
    }

    @PutMapping
    public ResponseEntity<Order> createOrder(@RequestBody Order order) {
        if(order.getId() == null) {
            return new ResponseEntity<Order>(orderService.addOrder(order), HttpStatus.OK);
        }
        LOGGER.severe("Failed to create an order with passed id. Order creation should not use external ids");
        return new ResponseEntity<Order>(HttpStatus.BAD_REQUEST);
    }

    @PostMapping
    public ResponseEntity<Order> updateOrder(@RequestBody Order order) {
        if(order.getId() == null) {
            LOGGER.severe("Can't update order without id — null value was passed instead of it");
            return new ResponseEntity<Order>(HttpStatus.BAD_REQUEST);
        }

        try {
            return new ResponseEntity<Order>(orderService.updateOrder(order), HttpStatus.OK);
        } catch (OrderNotFoundException e) {
            LOGGER.severe("Can`t update an order with non-existing id" + order.getId());
            return new ResponseEntity<Order>(HttpStatus.NOT_FOUND);
        }

    }

}
