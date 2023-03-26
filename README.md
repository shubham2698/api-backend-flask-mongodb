<h3>FLASK BACKEND API MONGODB</h3>
<h4>Use postman post call API</br>pass json or form data through body </h4>
<ul>
    <li>insert data. call api http://127.0.0.1:5000/insert </br>pass this in body</br>
    {
     "name": "MILk",
     "type": "LIQUID",
     "unit": "1,10,100"
    }</li>
    <li>update data. call api http://127.0.0.1:5000/update </br>pass this in body</br>
    {
     "key": "PINEAPPLE",
     "col": "PRODUCT_TYPE",
     "value": "LIQUID"
    }</li>
    <li>delete data. call api http://127.0.0.1:5000/delete </br>pass this in body</br>
    {
     "key": "MILK"
    }</li>
    <li>view data. call api http://127.0.0.1:5000/view</li>

</ul>

<p>
    Collection Data:
    </br>
    {</br>
        "apple":{</br>
            "PRODUCT_TYPE":"solid",</br>
            "PRODUCT_UNIT":"1, 12, 24",</br>
            "SUB_PRODUCT":"1 apple, 12 apple, 24 apple"</br>
        },</br>
        "pineapple":{</br>
            "PRODUCT_TYPE":"solid",</br>
            "PRODUCT_UNIT":"1, 12, 24",</br>
            "SUB_PRODUCT":"1 apple, 12 apple, 24 apple"</br>
        }</br>
    }</br>

    *derived attribute : subproduct from key+unit; 
</p>