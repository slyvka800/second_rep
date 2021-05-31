package ua.lviv.iot.disposable_tableware.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ua.lviv.iot.disposable_tableware.models.*;
import ua.lviv.iot.disposable_tableware.service.GlassService;

import javax.management.InstanceNotFoundException;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.logging.Logger;


@RestController
@RequestMapping(path = "/glass")
public class GlassController {

    private static final Logger LOGGER = Logger
            .getLogger("ua.lviv.iot.disposable_tableware.controller.GlassController");

    @Autowired
    private GlassService glassService;

    @GetMapping(path = "/{id}")
    public ResponseEntity<Glass> getGlass(@PathVariable Integer id) {
        try {
            return new ResponseEntity<Glass>(glassService.getGlass(id), HttpStatus.OK);
        } catch (NoSuchElementException e) {
            LOGGER.severe("Failed to get a glass with passed id");
            return new ResponseEntity<Glass>(HttpStatus.NOT_FOUND);
        }

    }

    @GetMapping
    public List<Glass> getGlasses() {
        return glassService.getGlasses();
    }

    @PostMapping
    public ResponseEntity<Glass> addGlass(@RequestBody Glass glass) {
        if (glass.getId() == 0) {
            return new ResponseEntity<Glass>(glassService.addGlass(glass), HttpStatus.OK);
        }

        LOGGER.severe("Failed to create a glass with passed id. Glass shouldn't have its own id");
        return new ResponseEntity<Glass>(HttpStatus.BAD_REQUEST);
    }

    @PutMapping
    public ResponseEntity<Glass> updateGlass(@RequestBody Glass glass) {
        if (glass.getId() == 0) {
            LOGGER.severe("Failed to update a glass without id. Glass should have external id");
            return new ResponseEntity<Glass>(HttpStatus.BAD_REQUEST);
        }

        try {
            return new ResponseEntity<Glass>(glassService.updateGlass(glass), HttpStatus.OK);
        } catch (InstanceNotFoundException e) {
            LOGGER.severe("Failed to update non-existing glass ");
            return new ResponseEntity<Glass>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping(path = "/{id}")
    public ResponseEntity<Glass> deleteGlass(@PathVariable Integer id) {

        try {
            return new ResponseEntity<Glass>(glassService.deleteGlass(id), HttpStatus.OK);
        } catch (InstanceNotFoundException e) {
            LOGGER.severe("Failed to delete non-existing glass ");
            return new ResponseEntity<Glass>(HttpStatus.NOT_FOUND);
        }

    }
}
