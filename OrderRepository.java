package ua.lviv.iot.shopping_project.dal;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ua.lviv.iot.shopping_project.models.Order;

@Repository
public interface OrderRepository extends JpaRepository<Order, Integer> {

}
