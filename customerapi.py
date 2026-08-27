from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field, field_validator
from databasefastapi import get_db

router = APIRouter(
            prefix="/customer",
            tags=["Customer"]
)

class CustomersCreate(BaseModel):
    phone_number: str = Field(min_length=10,
                              max_length=10
    )
    name: str
    password: str = Field(min_length=6,
                          max_length=10
                          )

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        return value
    
class CustomerUpdate(BaseModel):
    name: str
    phone_number : str = Field(
        min_length=10,
        max_length=10
    )

    @field_validator("phone_number")
    @classmethod
    def vlaidate_phone_number(cls, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain digits")
        return value

class CustomerResponse(BaseModel):
    id: int
    phone_number: str
    name: str



#----------------------------------------------------------------
#Add Customers
#----------------------------------------------------------------

@router.post("/", status_code=201)
def create_cust(customer: CustomersCreate, conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Customers(phone_number, name, password)
        VALUES (?, ?, ?)
    """,(
        customer.phone_number,
        customer.name,
        customer.password
    ))

    conn.commit()

    return{"message": "Employee added successfully"}

#-----------------------------------------------------------------
# Fetch Customers
#-----------------------------------------------------------------

@router.get("/",
            response_model=list[CustomerResponse])
def get_cust(conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM Customers
    """)

    rows = cursor.fetchall()

    customers = []

    for row in rows:
        customers.append({
            "id": row[0],
            "phone_number": row[1],
            "name": row[2]
        })


    return customers

#-----------------------------------------------------------
# Fetch Customer by Id
#-----------------------------------------------------------

@router.get("/{id}",
            response_model=CustomerResponse
            )
def get_custm(id: int, conn=Depends(get_db)):

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Customers
        WHERE id = ?
    """, (id,))

    row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Cusotmer not found"
        )

    return{
        "id": row[0],
        "phone_number": row[1],
        "name": row[2]
    }

#-----------------------------------------------------------
# Update Customers
#-----------------------------------------------------------

@router.put("/{id}")
def update_cust(id: int,customer: CustomerUpdate, conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Customers
        SET name = ?, phone_number = ?
        WHERE id = ?
    """,(
        customer.name,
        customer.phone_number,
        id
    ))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    conn.commit()

    return {
        "message": "Customer updated successfully"
    }

#-----------------------------------------------------------------
#Delete Customer
#-----------------------------------------------------------------

@router.delete("/{id}")
def delete_custm(id: int, conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Customers
        WHERE id = ?
    """, (id,))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    conn.commit()

    return {
        "message": "Customer deleted successfully"
    }

