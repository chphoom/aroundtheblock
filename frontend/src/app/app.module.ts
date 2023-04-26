import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { JwtModule } from '@auth0/angular-jwt';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { StatsComponent } from './stats/stats.component';
import { MeChallengeComponent } from './me-challenge/me-challenge.component';
import { LoginComponent } from './login/login.component';


import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { HttpRequestInterceptor } from './http-request.interceptor';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCardModule } from '@angular/material/card';
import { MatTabsModule } from '@angular/material/tabs';
import { MatInputModule } from '@angular/material/input';
import { MatGridListModule } from '@angular/material/grid-list';
import { ProfileComponent } from './profile/profile.component';
import { NavigationComponent } from './navigation/navigation.component';
import { FooterComponent } from './footer/footer.component';
import { WeChallengeComponent } from './we-challenge/we-challenge.component';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { AboutComponent } from './about/about.component';
import { PastChallengesComponent } from './past-challenges/past-challenges.component';
import { GeneratedComponent } from './me-challenge/generated/generated.component';
import { UploadComponent } from './upload/upload.component';
import { PostComponent } from './post/post.component';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { SearchComponent } from './search/search.component';
import { EditProfileComponent } from './profile/edit-profile/edit-profile.component';
import { MatSnackBarModule } from '@angular/material/snack-bar';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    StatsComponent,
    MeChallengeComponent,
    LoginComponent,
    ProfileComponent,
    NavigationComponent,
    FooterComponent,
    WeChallengeComponent,
    AboutComponent,
    PastChallengesComponent,
    GeneratedComponent,
    UploadComponent,
    PostComponent,
    SearchComponent,
    EditProfileComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatIconModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatFormFieldModule,
    FormsModule,
    MatCardModule,
    MatTabsModule,
    MatInputModule,
    MatGridListModule,
    MatCheckboxModule,
    MatProgressSpinnerModule,
    MatSnackBarModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: () => {
          return localStorage.getItem("authToken")
        }
      }
    }),
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: HttpRequestInterceptor,
    multi: true,
  }],
  bootstrap: [AppComponent]
})
export class AppModule {}