package ua.lviv.iot.disposable_tableware.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ua.lviv.iot.disposable_tableware.models.*;
import ua.lviv.iot.disposable_tableware.service.GlassService;

import java.lang.management.GarbageCollectorMXBean;
import java.util.List;


@RestController
@RequestMapping(path = "/glass")
public class GlassController {

    @Autowired
    private GlassService glassService;

    @GetMapping(path = "/{id}")
    public Glass getGlass(@PathVariable Integer id) {
        return glassService.getGlass(id);
    }

    @GetMapping
    public List<Glass> getGlasses() {
        return glassService.getGlasses();
    }

    @PostMapping
    public Glass addGlass(@RequestBody Glass glass) {
        return glassService.addGlass(glass);
    }

    @PutMapping
    public ResponseEntity<Glass> updateGlass(@RequestBody Glass glass)
    {
        if(glassService.getGlass(glass.getId()) != null) {
            return new ResponseEntity<Glass>(glassService.updateGlass(glass), HttpStatus.OK);
        } else {
            return new ResponseEntity<Glass>(HttpStatus.NOT_FOUND);
        }
    }

    @PutMapping(path = "/{id}")
    public ResponseEntity<Glass> updateGlass(@PathVariable Integer id, @RequestBody Glass glass) {
        if(glassService.getGlass(id) != null) {
            return new ResponseEntity<Glass>(glassService.updateGlass(id, glass), HttpStatus.OK);
        } else {
            return new ResponseEntity<Glass>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping(path = "/{id}")
    public ResponseEntity<Glass> deleteGlass(@PathVariable Integer id) {
        if(glassService.getGlass(id) != null) {
            return new ResponseEntity<Glass>(glassService.deleteGlass(id), HttpStatus.OK);
        } else {
            return new ResponseEntity<Glass>(HttpStatus.NOT_FOUND);
        }
    }
}
