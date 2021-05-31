package ua.lviv.iot.disposable_tableware.dal;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ua.lviv.iot.disposable_tableware.models.Glass;


@Repository
public interface GlassRepository extends JpaRepository<Glass, Integer> {
}
