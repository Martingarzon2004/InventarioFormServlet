package mx.inventario.dao;

import com.inventario.domain.Listadeproducos;
import org.springframework.data.repository.CrudRepository;

public interface IlistadeproductosDAO extends CrudRepository<Listadeproducos, Long>{
    
}
