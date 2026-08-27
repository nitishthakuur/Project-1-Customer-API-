from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from databasefastapi import get_db

router = APIRouter(
            prefix="/customer",
            tags=["Customer"]
)

class CustomersCreate(BaseModel):
    id: int
    phone_number: str = Field(min_length=10,
                              max_length=10
    )
    name: str
    passward: str = Field(min_length=6,
                          max_length=10
                          )


class CustomerUpdate(BaseModel):
    name: str
    phone_number : str
    name: str

class CustomerResponse(BaseModel):
    name: str



#----------------------------------------------------------------
#Add Customers
#----------------------------------------------------------------

@router.post("/", status_code=201)
def create_cust(customer: CustomersCreate, conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Customers(id, phone_number, name, passward)
        VALUES (?, ?, ?, ?)
    """,(
        customer.id,
        customer.phone_number,
        customer.name,
        customer.passward
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
        customers.append(
            {"name": row[2]}
        )


    return customers

#-----------------------------------------------------------
# Fetch Customer by Id
#-----------------------------------------------------------

@router.get("/", {id},
            response_model=CustomerResponse
            )
def get_custm(id: int, conn=Depends(get_db)):

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Customers
        WHERE id = ?
    """, (id,))

    row = cursor.fetchone()

    return{
        "name": row[2]
    }

#-----------------------------------------------------------
# Update Customers
#-----------------------------------------------------------

@router.put("/",{id})
def update_cust(id: int,customer: CustomerUpdate, conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Customers
        SET name = ?
        WHERE id = ?
    """,(
        customer.name,
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

@router.delete("/", {id})
def delete_custm(id: int, conn=Depends(get_db)):

    cursor = conn.cursor()

    cursor.execute("""
        DELETE Customers
        WHERE id = ?
    """, (id,))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer not found"
    }

