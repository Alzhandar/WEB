import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';  
import { AppRoutingModule } from './app-routing.module';
import { CompanyListComponent } from './components/company-list/company-list.component';  
import { VacancyListComponent } from './components/vacancy-list/vacancy-list.component';  

@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,  
    VacancyListComponent    
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule 
  ],
  providers: [],
  bootstrap: [AppComponent]  
})
export class AppModule { }
