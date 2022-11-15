

#include <bits/stdc++.h>
// #include <windows.h>
using namespace std;


void welcome(){
    cout << endl << endl ;
    cout << "\t\t\t---------- Welcome to LA'OPALA CAFE ---------- \n" << endl;
}


//Wait function
// void wait_func()
// {
//   cout<<"Please Wait ";
//   for(int i = 0 ; i < 3 ; i++){
//     cout<<".";
//     Sleep(1000);
//   }
//   cout << endl ;
// }


bool verify_password(char *p)
{
  // check if the length is insufficient
  int length = strlen(p);
  if (length < 8) return false;
  
  bool has_upper = false;
  bool has_lower = false;
  bool has_digit = false;
  bool has_symbol = false;
  
  // check for each of the required character classes
  for (int i = 0; i < length; i++){
    if (islower(p[i])) has_lower = true;
    if (isdigit(p[i])) has_digit = true;
    if (isupper(p[i])) has_upper = true;
    if (ispunct(p[i])) has_symbol = true;
  }
  
  // return false if any required character class is not present
  if (!has_upper) return false;
  if (!has_lower) return false;
  if (!has_digit) return false;
  if (!has_symbol) return false;
  
  // if we couldn't invalidate the password it must be valid
  return true;
}

void sign_up(string &password, string &contact_num,string &name){
  cout << "\t\t\t     ----- SIGN UP YOUR NEW ACCOUNT ----- \n" << endl ;
  cout << "Enter your Name : ";
  cin >> name ;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  cout << "Enter your contact number : " ;
  cin >> contact_num ;
  cout << endl ;
  label:
  cout << "Create a password(must be minimum 8 characters , must include special character , upper case and lower case alphabets and number) : \n" ;
  cin >> password ;
  cout << endl ;
  char p[50];
  for(int i = 0 ; i < password.length() ; i++ )
  {
    p[i] = password[i] ;
  }
 bool result = verify_password(p);
  if (result) printf("Verified password!\n\n");
  else {
    printf("Invalid password! \n");
    goto label;
  }
}

void log_in(string &password, string &contact_num, string &address,string &name){
  string contact_verify , password_verify ;
  cout << "\t\t\t---------- LOG IN TO YOUR ACCOUNT ---------- \n" << endl ;
  label:
  cout << "Enter contact number : " ;
  cin >> contact_verify ;
  cout << "Enter Password : " ;
  cin >> password_verify ;
  cout << endl ;
  cout << endl ;
  if((contact_num==contact_verify)&&(password==password_verify)){
    cout << "Account Verified. Logging in ...";
    cout << endl ;
    //wait_func();
    cout << "Welcome " << name << endl << endl  ;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
 
    cout << "Enter your delivery address : " ;
    cin >> address ;   
  }
  else{
    cout << "Try Again " << endl ;
    goto label;
  }

}

void menu_card(vector<string> &fmenu,vector<int> &price, vector<string> &cart_items,vector <int> &cart_prices,vector <int> &cart_quantity,int quantity, int order){

  while(true)
  {
        int choice ;

        label:
        cout << endl << endl << " ---------- Food Menu ---------- \n" << endl;
        
        for (int i = 0; i < 10; i++)
        {

          // Showing food menu to customer
          cout << i + 1 << ". " << fmenu[i] << endl;

        }

        cout << "\nSelect the food you want to order : ";

        // Taking order from customer
        cin >> order;

        cout << "\nYou have selected " << fmenu[order - 1] << endl;

        cout << "\nHow many you want to order ? : ";
        // Taking quantity of food
        cin >> quantity;
     
        cout<< endl ;

        cart_items.push_back(fmenu[order - 1]) ;
        cart_prices.push_back(price[order - 1]) ;
        cart_quantity.push_back(quantity) ;
       
        
        cout << "Would you like to order anything else ? \n\n" ;
        cout << "Press 1 for Yes or Press 0 for No.\n" ;
        cin>>choice ;
        cout<<endl;
        if(choice){
          goto label;
        }
        else{
          break;
        }
       
  }

}


void payment(int &total_price){
  string coupon ;
  cout<< "Enter FIRST15 to get 15% off on your first order .\n\n";
  cin >> coupon ;
  if(coupon == "FIRST15" || coupon == "first15"){
      total_price = total_price - 0.15*total_price ;
  }
  cout << "You need to pay Rs. "<< total_price ;
   
}


void show_payment_bill(vector<string> &cart_items,vector <int> &cart_prices,vector <int> &cart_quantity){
  int total_price = 0 ;
  cout << "--------------- YOUR BILL ---------------";
  cout << endl ;
  cout << endl ;
  cout << "Ordered Items\t" <<"     |        " << " Price x Quantity" ;
  cout << endl ;
  cout << endl ;

  for(int i = 0 ; i < cart_items.size() ; i++ )
  {
     total_price = total_price + cart_prices[i]*cart_quantity[i] ;
     cout << cart_items[i] ;

     for(int j=0;j<=(20-cart_items[i].size());j++){
        cout<<" ";
     }
      cout<<"|         "<<"Rs. " << cart_prices[i] << " x " << cart_quantity[i] << endl;
      
  }
  cout << "--------------------------------------------\n";
     
      cout << "TOTAL                :         "<<"Rs. " << total_price ;

      cout << endl ;
      cout << endl ;
      options :
      cout << "(C) APPLY COUPON\t(P) MAKE PAYMENT\t (E) EXIT" ;
      cout << endl ;

      char inp2 ;
      cin >> inp2 ;

      options_3 :
      if(toupper(inp2) == 'C'){
          payment(total_price) ;
      }
      else if(toupper(inp2) == 'P'){
        cout << "You need to pay Rs. " << total_price ;
      }
      else if(toupper(inp2) == 'E'){
        exit(0);
      }
      else {
        cout << "Invalid Input . Try Again !\n" ;
        goto options_3 ;
      }

}


int main()
{
  string password ;
  string contact_num ;
  vector <string> cart_items;
  vector <int> cart_prices;
  vector <int> cart_quantity;
  int order, quantity, cpayment;
  string name, delivery, paymentnum, transid, address ;
  // Storing list of foods in string type array "fmenu"
  vector <string> fmenu =
  {
    "Burger",
    "Coke",
    "Cold Coffee",
    "Pizza",
    "Crispy Corn",
    "French Fries",
    "Americano Coffee",
    "Ice Cream",
    "Latte",
    "Momos"
};
  // Storing prices of foods in integer type array "price"
  vector<int> price =
  {

    100,
    40,
    99,
    249,
    149,
    80,
    150,
    100,
    149,
    179

  };


char inp ;


welcome();



sign_up(password,contact_num,name);
//wait_func();
log_in(password,contact_num,address,name);

menu_card(fmenu,price,cart_items,cart_prices,cart_quantity,quantity,order);

options :
cout<< "(E) EXIT \t\t (P) PAYMENT" << endl ;

cin >> inp ;



if(toupper(inp) == 'E'){
  exit(0);
}
else if (toupper(inp) == 'P'){
  show_payment_bill(cart_items,cart_prices,cart_quantity);
}
else {
  cout << "Invalid Input . Try Again !\n" ;
  goto options ;

}
  cout<< endl ;
  cout << "Reaching you in 27 minutes !";
  cout << endl ;
  
  cout << "\nThank you for choosing us. \nENJOY YOUR SNACK! :)\n";
  cout << endl ;
  cout << endl ;


  return 0;
}

