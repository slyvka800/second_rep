package ua.lviv.iot.disposable_tableware.service;

import org.springframework.stereotype.Service;
import org.springframework.web.context.annotation.ApplicationScope;
import ua.lviv.iot.disposable_tableware.models.Glass;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;


@Service
@ApplicationScope
public class GlassService {

    private AtomicInteger id = new AtomicInteger(0);

    private Map<Integer, Glass> glassMap = new HashMap<Integer, Glass>();

    public Glass addGlass(Glass glass) {
        Integer glassId = id.incrementAndGet();
        glass.setId(glassId);
        glassMap.put(glassId, glass);
        return glass;
    }

    public List<Glass> getGlasses() {
        return new ArrayList<>(glassMap.values());
    }

    public Glass getGlass(Integer id) {
        return glassMap.get(id);
    }

    public Glass updateGlass(Glass glass) {
        return glassMap.put(glass.getId(), glass);
    }

    public Glass updateGlass(Integer id, Glass glass) {
        return glassMap.put(id, glass);
    }

    public Glass deleteGlass(Integer id) {
        return glassMap.remove(id);
    }
}
