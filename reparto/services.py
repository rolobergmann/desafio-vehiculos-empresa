from .models import Vehiculo, Chofer, RegistroContabilidad

class ServiciosApp:
    # ... Otros servicios

    def crear_vehiculo(self, patente, marca, modelo, year):
        try:
            Vehiculo.objects.create(
                patente=patente, marca=marca, modelo=modelo, year=year
            )
            return True  # Indicar éxito
        except Exception as e:  # Considerar un manejo de excepciones más específico
            print(f"Error creando vehiculo: {e}")
            return False

    def crear_chofer(self, rut, nombre, apellido, activo, vehiculo_id):
        try:
            Chofer.objects.create(
                rut=rut, nombre=nombre, apellido=apellido, activo=False, vehiculo_id=vehiculo_id)
        except Exception as e: 
            print(f"Error creando chofer: {e}")
            return False 
    def crear_registro_contable(self, vehiculo_id, valor, fecha_compra):
        try:
            RegistroContabilidad.objects.create(
                vehiculo_id=vehiculo_id, valor=valor, fecha_compra=fecha_compra
            )
            return True  # Indicar éxito
        except Exception as e:
            print(f"Error creando registro contable: {e}")
            return False
        
    def deshabilitar_chofer(self, rut):
        try:
            chofer = Chofer.objects.get(rut=rut)
            chofer.activo = False
            chofer.save()
            return True  # Indicar éxito
        except Chofer.DoesNotExist:
            return False  # Chofer no encontrado
        except Exception as e:
            print(f"Error deshabilitando chofer: {e}")
            return False

    def deshabilitar_vehiculo(self, patente):
        try:
            vehiculo = Vehiculo.objects.get(patente=patente)
            vehiculo.activo = False
            vehiculo.save()
            return True  # Indicar éxito
        except Vehiculo.DoesNotExist:
            return False  # Vehiculo no encontrado  
        except Exception as e:
            print(f"Error deshabilitando vehiculo: {e}")

    def habilitar_chofer(self, rut):
        try:
            chofer = Chofer.objects.get(rut=rut)
            chofer.activo = True
            chofer.save()
            return True #Indicar exito
        except Chofer.DoesNotExist:
            return False #Chofer no encontrado
        except Exception as e:
            print(f"Error habilitando chofer: {e}")
            return False
    
    def habilitar_vehiculo(self, patente):
        try:
            vehiculo = Vehiculo.objects.get(patente=patente)
            vehiculo.activo = True
            vehiculo.save()
            return True #Indicar exito
        except Vehiculo.DoesNotExist:
            return False # Vehiculo no encontrado
        except Exception as e:
            print(f"Error habilitando vehiculo: {e}")
            return False

    def obtener_vehiculo(self, patente):
        try:
            return Vehiculo.objects.get(patente=patente)
        except Vehiculo.DoesNotExist:
            return None
    
    def obtener_chofer(self, rut):
        try:
            return Chofer.objects.get(rut=rut)
        except Chofer.DoesNotExist:
            return None
        
    def asignar_chofer_a_vehiculo(self, patente, rut):
        try:
            vehiculo = Vehiculo.objects.get(patente=patente)
            chofer = Chofer.objects.get(rut=rut)
            vehiculo.chofer = chofer
            vehiculo.save()
            return True  # Asignación exitosa
        except (Vehiculo.DoesNotExist, Chofer.DoesNotExist):
            return False  # Vehiculo o chofer no encontrado
        except Exception as e:
            print(f"Error asignando chofer a vehiculo: {e}")
            return False  # Error al asignar el chofer a vehiculo
    
    def imprimir_datos_vehiculos(self):
        vehiculos = Vehiculo.objects.all()
        for vehiculo in vehiculos:
            print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}")