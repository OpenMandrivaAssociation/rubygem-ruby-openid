%define	oname	ruby-openid

Summary:	A library for consuming and serving OpenID identities
Name:		rubygem-%{oname}
Version:	2.1.7
Release:	%mkrel 1
License:	ASL 2.0
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
Ruby OpenID is a Ruby library for verifying and serving OpenID identities.

==Features
* Easy to use API for verifying OpenID identites - OpenID::Consumer
* Support for serving OpenID identites - OpenID::Server
* Does not depend on underlying web framework
* Supports multiple storage mechanisms (Filesystem, ActiveRecord, Memory)
* Example code to help you get started, including:
  * Ruby on Rails based consumer and server
  * OpenIDLoginGenerator for quickly getting creating a rails app that uses
    OpenID for authentication
  * ActiveRecordOpenIDStore plugin
* Comprehensive test suite
* Supports both OpenID 1 and OpenID 2 transparently

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

