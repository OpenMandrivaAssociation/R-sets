%global packname  sets
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.13
Release:          3
Summary:          Sets, Generalized Sets, Customizable Sets and Intervals
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/sets_1.0-13.tar.gz
Requires:         R-stats 
Requires:         R-proxy 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-stats 
BuildRequires:    R-proxy 

%description
Data structures and basic operations for ordinary sets, generalizations
such as fuzzy sets, multisets, and fuzzy multisets, customizable sets, and

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_8-1
+ Revision: 777881
- Import R-sets
- Import R-sets



