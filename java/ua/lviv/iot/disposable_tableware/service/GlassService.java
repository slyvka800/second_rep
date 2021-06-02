package ua.lviv.iot.disposable_tableware.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.context.annotation.ApplicationScope;
import ua.lviv.iot.disposable_tableware.dal.GlassRepository;
import ua.lviv.iot.disposable_tableware.models.Glass;

import javax.management.InstanceNotFoundException;
import java.util.List;


@Service
@ApplicationScope
public class GlassService {

    @Autowired
    private GlassRepository repository;

    public Glass addGlass(Glass glass) {
        return repository.save(glass);
    }

    public List<Glass> getGlasses() {
        return repository.findAll();
    }

    public Glass getGlass(Integer id) {
        return repository.findById(id).orElseThrow();
    }

    public Glass updateGlass(Glass glass) throws InstanceNotFoundException{
        var oldGlass = repository.findById(glass.getId()).orElse(null);
        if(oldGlass == null) {
            throw new InstanceNotFoundException("You are trying to update non-existing glass");
        }
        repository.save(glass);
        return oldGlass;
    }

    public Glass deleteGlass(Integer id) throws InstanceNotFoundException{
        var deletingObject = repository.findById(id).orElse(null);
        if(deletingObject == null) {
            throw new InstanceNotFoundException("You are trying to delete non-existing glass");
        }
        repository.deleteById(id);
        return deletingObject;
    }
}
